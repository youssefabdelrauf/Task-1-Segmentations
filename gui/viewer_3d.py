import sys
import os
import vtk
import numpy as np
import SimpleITK as sitk
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtk.util import numpy_support

class VTK3DViewer(QWidget):
    def __init__(self, parent=None, organ_name="Default"):
        super().__init__(parent)
        self.organ_name = organ_name
        self.np_data = None
        self.spacing = (1.0, 1.0, 1.0)
        self.actor = None
        self.actors = {}  # Dictionary for multiple part actors
        self.vtk_initialized = False
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        try:
            # VTK Widget
            self.vtkWidget = QVTKRenderWindowInteractor(self)
            self.layout.addWidget(self.vtkWidget)
            
            self.renderer = vtk.vtkRenderer()
            self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)
            self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
            
            # Premium dark background (matches GUI theme)
            self.renderer.SetBackground(0.05, 0.05, 0.1)
            
            # Initialize (can be delayed, but this is standard)
            self.iren.Initialize()
            self.iren.Start()
            self.vtk_initialized = True
        except Exception as e:
            self.layout.addWidget(QLabel(f"VTK Initialization Failed: {e}"))
            print(f"VTK Init Error: {e}")
    
    def reset_viewer(self):
        """Clear the current 3D model to prepare for loading a new one."""
        if self.actor:
            self.renderer.RemoveActor(self.actor)
            self.actor = None
        # Clear all part actors
        for actor in self.actors.values():
            self.renderer.RemoveActor(actor)
        self.actors = {}
        self.np_data = None
        self.spacing = (1.0, 1.0, 1.0)
        self.origin = (0.0, 0.0, 0.0)
        if self.vtk_initialized:
            self.vtkWidget.GetRenderWindow().Render()
    
    def set_organ_name(self, name):
        """Update the organ name for color mapping."""
        self.organ_name = name

    def load_nifti(self, file_path):
        try:
            print(f"Loading NIfTI: {file_path}")
            img = sitk.ReadImage(file_path)
            # Reorient to standard orientation if possible
            img = sitk.DICOMOrient(img, 'LPS') 
            
            self.np_data = sitk.GetArrayFromImage(img)
            self.spacing = img.GetSpacing()
            self.origin = img.GetOrigin()
            
            # Downsample if too large to prevent freezing
            if max(self.np_data.shape) > 256:
                print(f"Downsampling large image: {self.np_data.shape}")
                self.np_data = self.np_data[::2, ::2, ::2]
                self.spacing = tuple(s * 2 for s in self.spacing)
            
            return True
        except Exception as e:
            print(f"Error loading NIfTI: {e}")
            return False

    def load_dicom(self, folder_path):
        try:
            reader = sitk.ImageSeriesReader()
            dicom_names = reader.GetGDCMSeriesFileNames(folder_path)
            reader.SetFileNames(dicom_names)
            img = reader.Execute()
            
            self.np_data = sitk.GetArrayFromImage(img)
            self.spacing = img.GetSpacing()
            return True
        except Exception as e:
            print(f"Error loading DICOM: {e}")
            return False

    def generate_hollow_3d(self, wall_thickness=2, opacity=0.7):
        if self.np_data is None: 
            print("No data to generate 3D")
            return False
        
        try:
            # Create VTK image data
            img_data = vtk.vtkImageData()
            depth, height, width = self.np_data.shape
            img_data.SetDimensions(width, height, depth)
            img_data.SetSpacing(self.spacing)
            img_data.SetOrigin(0, 0, 0)
            
            # Convert numpy to vtk array
            # Handle type mapping
            vtk_type = numpy_support.get_vtk_array_type(self.np_data.dtype)
            flat_data = self.np_data.reshape(-1, order='C') # 'C' is usually right for SimpleITK->VTK if dims match
            
            # Important: VTK expects data in F-contiguous (Fortran) order for X,Y,Z structure
            # But SimpleITK returns Z,Y,X. We must permute or flatten correctly.
            # Easiest way: Permute numpy to X,Y,Z then flatten.
            data_perm = np.transpose(self.np_data, (2, 1, 0)) # Z,Y,X -> X,Y,Z
            flat_data = data_perm.flatten(order='F')
            
            vtk_array = numpy_support.numpy_to_vtk(num_array=flat_data, deep=True, array_type=vtk_type)
            img_data.GetPointData().SetScalars(vtk_array)
            
            # Dynamically find the target label (ignore 0)
            unique_labels = np.unique(self.np_data)
            valid_labels = [x for x in unique_labels if x > 0]
            
            if not valid_labels:
                print("Error: No segmentation labels found (image is empty/black).")
                return False
                
            target_label = valid_labels[0]
            print(f"Generating 3D surface for label: {target_label}")
            
            # Marching Cubes
            mc = vtk.vtkDiscreteMarchingCubes()
            mc.SetInputData(img_data)
            mc.ComputeNormalsOn()
            mc.GenerateValues(1, target_label, target_label)
            
            # Smooth
            smoother = vtk.vtkWindowedSincPolyDataFilter()
            smoother.SetInputConnection(mc.GetOutputPort())
            smoother.SetNumberOfIterations(15)
            smoother.BoundarySmoothingOff()
            smoother.FeatureEdgeSmoothingOff()
            smoother.SetPassBand(0.001)
            smoother.NonManifoldSmoothingOn()
            smoother.NormalizeCoordinatesOn()
            smoother.Update()

            # Mapper
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(smoother.GetOutputPort())
            mapper.ScalarVisibilityOff()
            
            if self.actor:
                self.renderer.RemoveActor(self.actor)
                
            self.actor = vtk.vtkActor()
            self.actor.SetMapper(mapper)
            self.actor.GetProperty().SetOpacity(opacity)
            
            color = self.get_organ_color(self.organ_name)
            self.actor.GetProperty().SetColor(color)
            
            # Lighting
            self.actor.GetProperty().SetSpecular(0.5)
            self.actor.GetProperty().SetSpecularPower(20)
            
            self.renderer.AddActor(self.actor)
            self.renderer.ResetCamera()
            self.vtkWidget.GetRenderWindow().Render()
            return True
        except Exception as e:
            print(f"Error generating 3D: {e}")
            import traceback
            traceback.print_exc()
            return False

    def get_organ_color(self, name):
        colors = {
            "Liver": (0.9, 0.4, 0.4),      # Red/Pink
            "Kidneys": (0.8, 0.6, 0.2),    # Brownish/Orange
            "Stomach": (0.9, 0.6, 0.7),    # Pink
            "Spleen": (0.6, 0.4, 0.6),     # Purple
            "Heart": (1.0, 0.0, 0.0),      # Red
            "Lungs": (0.9, 0.9, 1.0)       # Pale Blue
        }
        return colors.get(name, (0.8, 0.8, 0.8))

    def add_part_from_nifti(self, file_path, part_name, color, opacity=0.7):
        """Load a NIfTI file as a separate part/actor."""
        try:
            print(f"Loading part {part_name} from: {file_path}")
            img = sitk.ReadImage(file_path)
            img = sitk.DICOMOrient(img, 'LPS')
            
            np_data = sitk.GetArrayFromImage(img)
            spacing = img.GetSpacing()
            
            # Downsample if too large
            if max(np_data.shape) > 256:
                np_data = np_data[::2, ::2, ::2]
                spacing = tuple(s * 2 for s in spacing)

            depth, height, width = np_data.shape
            
            # Create VTK image data
            img_data = vtk.vtkImageData()
            img_data.SetDimensions(width, height, depth)
            img_data.SetSpacing(spacing)
            img_data.SetOrigin(0, 0, 0)
            
            vtk_type = numpy_support.get_vtk_array_type(np_data.dtype)
            data_perm = np.transpose(np_data, (2, 1, 0))
            flat_data = data_perm.flatten(order='F')
            
            vtk_array = numpy_support.numpy_to_vtk(num_array=flat_data, deep=True, array_type=vtk_type)
            img_data.GetPointData().SetScalars(vtk_array)
            
            # Find target label
            unique_labels = np.unique(np_data)
            valid_labels = [x for x in unique_labels if x > 0]
            if not valid_labels:
                print(f"No label found in {file_path}")
                return False
            target_label = valid_labels[0]
            
            # Marching Cubes
            mc = vtk.vtkDiscreteMarchingCubes()
            mc.SetInputData(img_data)
            mc.ComputeNormalsOn()
            mc.GenerateValues(1, target_label, target_label)
            
            # Smooth
            smoother = vtk.vtkWindowedSincPolyDataFilter()
            smoother.SetInputConnection(mc.GetOutputPort())
            smoother.SetNumberOfIterations(15)
            smoother.BoundarySmoothingOff()
            smoother.FeatureEdgeSmoothingOff()
            smoother.SetPassBand(0.001)
            smoother.NonManifoldSmoothingOn()
            smoother.NormalizeCoordinatesOn()
            smoother.Update()
            
            # Mapper
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(smoother.GetOutputPort())
            mapper.ScalarVisibilityOff()
            
            # Actor
            actor = vtk.vtkActor()
            actor.SetMapper(mapper)
            actor.GetProperty().SetOpacity(opacity)
            actor.GetProperty().SetColor(color)
            actor.GetProperty().SetSpecular(0.5)
            actor.GetProperty().SetSpecularPower(20)
            
            self.actors[part_name] = actor
            self.renderer.AddActor(actor)
            
            self.renderer.ResetCamera()
            self.vtkWidget.GetRenderWindow().Render()
            return True
            
        except Exception as e:
            print(f"Error adding part {part_name}: {e}")
            return False


    def set_part_opacity(self, part_name, val):
        """Set opacity for a specific part (0-100)."""
        if part_name in self.actors:
            self.actors[part_name].GetProperty().SetOpacity(val / 100.0)
            self.vtkWidget.GetRenderWindow().Render()

    def set_part_color(self, part_name, color_tuple):
        """Set color for a specific part."""
        if part_name in self.actors:
            self.actors[part_name].GetProperty().SetColor(color_tuple)
            self.vtkWidget.GetRenderWindow().Render()

    def set_part_visibility(self, part_name, visible):
        """Set visibility for a specific part."""
        if part_name in self.actors:
            self.actors[part_name].SetVisibility(visible)
            self.vtkWidget.GetRenderWindow().Render()

    def set_opacity(self, val):
        if self.actor:
            self.actor.GetProperty().SetOpacity(val / 100.0) # Assume 0-100 input
            self.vtkWidget.GetRenderWindow().Render()

    def set_color(self, color_q):
        if self.actor:
            self.actor.GetProperty().SetColor(color_q.redF(), color_q.greenF(), color_q.blueF())
            self.vtkWidget.GetRenderWindow().Render()

    def set_visibility(self, visible):
        if self.actor:
            self.actor.SetVisibility(visible)
            self.vtkWidget.GetRenderWindow().Render()
