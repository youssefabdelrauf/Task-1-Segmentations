import sys
import os
import numpy as np
import SimpleITK as sitk
import vtk
from vtk.util import numpy_support
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import scipy.ndimage as ndimage  # <--- Added for Hollowing

from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QWidget, QFileDialog, QFrame, QLabel, QSplitter, QMessageBox, QInputDialog)
from PyQt5.QtCore import Qt

class MRIViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Viewer Pro (Hollow 3D)")
        self.resize(1200, 800)

        # Data placeholders
        self.sitk_image = None
        self.np_data = None
        self.spacing = None

        # --- Main Layout ---
        self.main_layout = QHBoxLayout(self)
        self.splitter = QSplitter(Qt.Horizontal)
        self.main_layout.addWidget(self.splitter)

        # --- Left Panel: Controls ---
        self.control_panel = QWidget()
        self.control_layout = QVBoxLayout(self.control_panel)
        
        # 1. Load Buttons
        self.btn_load_nifti = QPushButton("Load NIfTI File (.nii)")
        self.btn_load_nifti.clicked.connect(self.load_nifti)
        
        self.btn_load_dicom = QPushButton("Load DICOM Folder")
        self.btn_load_dicom.clicked.connect(self.load_dicom)

        # 2. Clear Button
        self.btn_clear = QPushButton("Clear / Reset Viewer")
        self.btn_clear.setStyleSheet("background-color: #ffcccc; color: darkred;")
        self.btn_clear.clicked.connect(self.reset_viewer)
        
        # 3. 3D Action
        self.btn_show_3d = QPushButton("Generate Hollow 3D")
        self.btn_show_3d.clicked.connect(self.generate_3d_mesh)
        
        self.lbl_status = QLabel("Status: Ready")
        self.lbl_status.setWordWrap(True)

        # Add widgets to layout
        self.control_layout.addWidget(self.btn_load_nifti)
        self.control_layout.addWidget(self.btn_load_dicom)
        self.control_layout.addWidget(self.btn_clear)
        self.control_layout.addSpacing(20)
        self.control_layout.addWidget(self.btn_show_3d)
        self.control_layout.addWidget(self.lbl_status)
        self.control_layout.addStretch()

        # --- Right Panel: VTK Viewer ---
        self.vtk_frame = QFrame()
        self.vtk_layout = QVBoxLayout(self.vtk_frame)
        self.vtkWidget = QVTKRenderWindowInteractor(self.vtk_frame)
        self.vtk_layout.addWidget(self.vtkWidget)

        self.renderer = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
        self.renderer.SetBackground(0.1, 0.1, 0.1) 

        self.splitter.addWidget(self.control_panel)
        self.splitter.addWidget(self.vtk_frame)
        self.splitter.setSizes([300, 900])

        self.iren.Initialize()

    def reset_viewer(self):
        """Clears all data and removes the 3D model."""
        self.sitk_image = None
        self.np_data = None
        self.spacing = None
        
        self.renderer.RemoveAllViewProps()
        self.vtkWidget.GetRenderWindow().Render()
        
        self.lbl_status.setText("Status: Viewer Cleared. Ready for new file.")

    def load_nifti(self):
        self.reset_viewer()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select NIfTI File", "", "NIfTI Files (*.nii *.nii.gz);;All Files (*)"
        )
        if file_path:
            try:
                self.sitk_image = sitk.ReadImage(file_path)
                self.process_image_data()
                self.lbl_status.setText(f"Loaded NIfTI:\n{os.path.basename(file_path)}")
            except Exception as e:
                self.lbl_status.setText(f"Error: {e}")

    def load_dicom(self):
        self.reset_viewer()
        folder_path = QFileDialog.getExistingDirectory(self, "Select DICOM Folder")
        
        if folder_path:
            try:
                reader = sitk.ImageSeriesReader()
                dicom_names = reader.GetGDCMSeriesFileNames(folder_path)
                
                if not dicom_names:
                    self.lbl_status.setText("Error: No DICOM series found in folder.")
                    return
                
                reader.SetFileNames(dicom_names)
                self.sitk_image = reader.Execute()
                self.process_image_data()
                self.lbl_status.setText(f"Loaded DICOM Series from:\n{os.path.basename(folder_path)}")
                
            except Exception as e:
                self.lbl_status.setText(f"DICOM Error: {e}")

    def process_image_data(self):
        self.np_data = sitk.GetArrayFromImage(self.sitk_image)
        self.spacing = self.sitk_image.GetSpacing()
        print(f"Data Shape: {self.np_data.shape}, Spacing: {self.spacing}")

    def generate_3d_mesh(self):
        if self.np_data is None:
            self.lbl_status.setText("Error: Load a file first.")
            return

        self.lbl_status.setText("Processing Hollow 3D... Please wait.")
        QApplication.processEvents() 

        # --- 1. HOLLOWING LOGIC START ---
        
        # Define Thickness (2 voxels is a safe default for visibility)
        wall_thickness = 2
        
        # Create a Binary Mask 
        # (Assuming your file is a segmentation where > 0 is the object)
        # If using raw MRI, you might want to raise this (e.g., > 200 for bone)
        mask = self.np_data > 0  
        
        # Create Structure for erosion (3D connectivity)
        struct = ndimage.generate_binary_structure(3, 1)
        
        # Erode (shrink) the mask
        eroded_mask = ndimage.binary_erosion(mask, structure=struct, iterations=wall_thickness)
        
        # Subtract eroded from original (XOR) to get the shell
        hollow_mask = mask ^ eroded_mask
        
        # Prepare data for VTK (Convert boolean mask back to uint8)
        data_matrix = hollow_mask.astype(np.uint8) 
        
        # --- HOLLOWING LOGIC END ---

        # 2. VTK Conversion
        vtk_data_array = numpy_support.numpy_to_vtk(
            num_array=data_matrix.ravel(), 
            deep=True, 
            array_type=vtk.VTK_UNSIGNED_CHAR
        )
        
        img_vtk = vtk.vtkImageData()
        img_vtk.SetDimensions(data_matrix.shape[2], data_matrix.shape[1], data_matrix.shape[0])
        img_vtk.SetSpacing(self.spacing[0], self.spacing[1], self.spacing[2])
        img_vtk.GetPointData().SetScalars(vtk_data_array)

        # 3. Marching Cubes
        dmc = vtk.vtkDiscreteMarchingCubes()
        dmc.SetInputData(img_vtk)
        dmc.GenerateValues(1, 1, 1) 

        # 4. Smoothing
        smoother = vtk.vtkWindowedSincPolyDataFilter()
        smoother.SetInputConnection(dmc.GetOutputPort())
        smoother.SetNumberOfIterations(15) 
        smoother.SetPassBand(0.005) 
        smoother.BoundarySmoothingOff()
        smoother.FeatureEdgeSmoothingOff()
        smoother.NonManifoldSmoothingOn()
        smoother.NormalizeCoordinatesOn()

        # 5. Rendering
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(smoother.GetOutputPort())
        mapper.ScalarVisibilityOff()

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # --- NEW CODE START ---
        # 1. Set Color to Dark Brown/Red (Liver)
        actor.GetProperty().SetColor(0.55, 0.25, 0.20) 

        # 2. Set Transparency (0.0 = Invisible, 1.0 = Solid)
        actor.GetProperty().SetOpacity(0.6) 

        # 3. Allow seeing the inside walls (Crucial for hollow models!)
        actor.GetProperty().BackfaceCullingOff()

        # 4. Make it look "wet" (Shiny)
        actor.GetProperty().SetSpecular(0.5)
        actor.GetProperty().SetSpecularPower(30)
        # --- NEW CODE END ---

        self.renderer.RemoveAllViewProps()
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()
        self.vtkWidget.GetRenderWindow().Render()
        
        self.lbl_status.setText("Status: Hollow Transparent Liver Generated")
        
        # Enable Backface Culling OFF so we can see inside if we clip into it
        actor.GetProperty().BackfaceCullingOff()
        
        actor.GetProperty().SetSpecular(0.3)
        actor.GetProperty().SetSpecularPower(20)

        self.renderer.RemoveAllViewProps()
        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()
        self.vtkWidget.GetRenderWindow().Render()
        
        self.lbl_status.setText("Status: Hollow 3D Generated")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = MRIViewer()
    viewer.show()
    sys.exit(app.exec_())