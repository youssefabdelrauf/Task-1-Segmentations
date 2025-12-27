import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QStackedWidget, 
                             QSlider, QCheckBox, QColorDialog, QFrame, QComboBox, 
                             QGridLayout, QGraphicsDropShadowEffect, QFileDialog)
from PyQt6.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve, QTimer
from PyQt6.QtGui import QColor, QFont, QPalette, QIcon, QPixmap, QLinearGradient, QBrush, QPainter, QPainterPath
import os

# Import 3D Viewer (optional - will work without VTK installed)
try:
    from viewer_3d import VTK3DViewer
    VTK_AVAILABLE = True
except ImportError:
    VTK_AVAILABLE = False
    print("VTK not available - 3D viewer will be disabled")

# --- PREMIUM GLASSMORPHISM COLOR PALETTE ---
THEME = {
    # Deep blue mesh gradient background (no purple)
    "bg_mesh_1": "#020812",           # Near black with blue tint
    "bg_mesh_2": "#041428",           # Deep navy
    "bg_mesh_3": "#0a1e3a",           # Rich sapphire blue
    "bg_mesh_4": "#061424",           # Deep ocean blue
    
    # Glassmorphism surfaces
    "glass_bg": "rgba(15, 15, 35, 0.6)",      # Frosted dark glass
    "glass_bg_hover": "rgba(25, 25, 55, 0.7)", # Hover state
    "glass_border": "rgba(100, 180, 255, 0.25)", # Luminous border
    "glass_border_glow": "rgba(100, 180, 255, 0.5)", # Brighter on hover
    
    # Glowing blue accents
    "accent": "#64B5FF",              # Primary glow blue
    "accent_bright": "#8DD4FF",       # Lighter blue
    "accent_deep": "#4A90E2",         # Deeper blue
    "accent_purple": "#A855F7",       # Purple accent
    "accent_cyan": "#22D3EE",         # Cyan highlight
    
    # Text hierarchy
    "text_primary": "#F8FAFC",        # Pure white text
    "text_secondary": "#94A3B8",      # Muted silver
    "text_glow": "#E0F2FE",           # Glowing text
    
    # Status colors
    "success": "#34D399",             # Emerald glow
    "warning": "#FBBF24",             # Amber glow
    "error": "#F87171",               # Soft red
    
    # Solid fallbacks
    "bg_solid": "#0a0a1a",
    "card_solid": "#12122a"
}

STYLE_SHEET = f"""
/* ===== MAIN WINDOW - MESH GRADIENT ===== */
QMainWindow {{ 
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 {THEME['bg_mesh_1']}, 
        stop:0.3 {THEME['bg_mesh_2']},
        stop:0.6 {THEME['bg_mesh_3']},
        stop:1 {THEME['bg_mesh_4']});
}}

/* ===== GLASSMORPHISM CARDS ===== */
QFrame#ControlCard {{ 
    background-color: {THEME['glass_bg']}; 
    border-radius: 20px; 
    border: 1px solid {THEME['glass_border']};
    padding: 20px;
}}

QFrame#ControlCard:hover {{
    border: 1px solid {THEME['glass_border_glow']};
}}

QFrame#GlassCard {{
    background-color: rgba(20, 20, 45, 0.5);
    border-radius: 16px;
    border: 1px solid {THEME['glass_border']};
}}

/* ===== TYPOGRAPHY ===== */
QLabel {{ 
    color: {THEME['text_primary']}; 
    font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Helvetica Neue', Arial, sans-serif;
    font-weight: 400;
}}

QLabel#Title {{
    font-size: 48px;
    font-weight: 800;
    color: {THEME['text_glow']};
    letter-spacing: -1px;
}}

QLabel#Subtitle {{
    font-size: 18px;
    color: {THEME['text_secondary']};
    letter-spacing: 0.3px;
    font-weight: 400;
}}

/* ===== ORGAN BUTTONS - GLOWING ICONS ===== */
QPushButton#OrganButton {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgba(30, 30, 60, 0.7), 
        stop:1 rgba(15, 15, 40, 0.8));
    border: 1px solid {THEME['glass_border']};
    border-radius: 20px;
    color: white;
    font-size: 15px;
    font-weight: 500;
}}

QPushButton#OrganButton:hover {{
    border: 2px solid {THEME['accent']};
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgba(50, 50, 100, 0.75), 
        stop:1 rgba(25, 25, 60, 0.85));
}}

QPushButton#OrganButton:pressed {{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgba(60, 60, 120, 0.85), 
        stop:1 rgba(30, 30, 70, 0.9));
    border: 2px solid {THEME['accent_bright']};
}}

/* ===== BACK BUTTON ===== */
QPushButton#BackButton {{
    background: transparent;
    border: 1px solid {THEME['glass_border']};
    border-radius: 12px;
    color: {THEME['text_secondary']};
    font-size: 14px;
    font-weight: 500;
    padding: 12px 24px;
}}

QPushButton#BackButton:hover {{
    border: 1px solid {THEME['accent']};
    color: {THEME['accent']};
    background: rgba(100, 181, 255, 0.1);
}}

/* ===== COLOR BUTTON ===== */
QPushButton#ColorBtn {{
    border-radius: 10px;
    font-weight: 600;
    padding: 12px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}}

QPushButton#ColorBtn:hover {{
    border: 1px solid rgba(255, 255, 255, 0.3);
}}

/* ===== COMBO BOX ===== */
QComboBox {{
    background-color: rgba(20, 20, 50, 0.6);
    color: {THEME['text_primary']};
    border: 1px solid {THEME['glass_border']};
    border-radius: 12px;
    padding: 12px 16px;
    font-size: 14px;
    font-weight: 500;
}}

QComboBox:hover {{
    border: 1px solid {THEME['accent']};
    background-color: rgba(30, 30, 70, 0.7);
}}

QComboBox::drop-down {{
    border: none;
    padding-right: 12px;
}}

QComboBox QAbstractItemView {{
    background-color: {THEME['card_solid']};
    color: {THEME['text_primary']};
    selection-background-color: {THEME['accent_deep']};
    border-radius: 10px;
    padding: 8px;
    border: 1px solid {THEME['glass_border']};
}}

/* ===== SLIDERS ===== */
QSlider::groove:horizontal {{
    height: 8px;
    background: rgba(100, 181, 255, 0.15);
    border-radius: 4px;
}}

QSlider::handle:horizontal {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 {THEME['accent_bright']}, 
        stop:1 {THEME['accent']});
    width: 20px;
    height: 20px;
    margin: -6px 0;
    border-radius: 10px;
    border: 2px solid rgba(255, 255, 255, 0.2);
}}

QSlider::handle:horizontal:hover {{
    background: {THEME['accent_bright']};
    border: 2px solid rgba(255, 255, 255, 0.4);
}}

QSlider::sub-page:horizontal {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {THEME['accent']}, 
        stop:1 {THEME['accent_cyan']});
    border-radius: 4px;
}}

/* ===== CHECKBOXES ===== */
QCheckBox {{
    color: {THEME['text_primary']};
    font-size: 13px;
    spacing: 10px;
}}

QCheckBox::indicator {{
    width: 22px;
    height: 22px;
    border-radius: 7px;
    border: 2px solid {THEME['glass_border']};
    background: rgba(20, 20, 50, 0.5);
}}

QCheckBox::indicator:checked {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 {THEME['accent']}, 
        stop:1 {THEME['accent_cyan']});
    border: 2px solid {THEME['accent_bright']};
}}

QCheckBox::indicator:hover {{
    border: 2px solid {THEME['accent']};
}}
"""

def add_shadow(widget, blur=25, offset=3, color=QColor(0, 0, 0, 120)):
    """Add a premium drop shadow for 3D depth."""
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(blur)
    shadow.setOffset(0, offset)
    shadow.setColor(color)
    widget.setGraphicsEffect(shadow)

def add_glow(widget, blur=40, color=QColor(100, 181, 255, 60)):
    """Add a subtle glow effect."""
    glow = QGraphicsDropShadowEffect()
    glow.setBlurRadius(blur)
    glow.setOffset(0, 0)
    glow.setColor(color)
    widget.setGraphicsEffect(glow)

class PartControl(QFrame):
    """Specific controls for one of the 3 organ parts."""
    def __init__(self, name, initial_color):
        super().__init__()
        self.setObjectName("ControlCard")
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        # Part Title & Visibility
        header = QHBoxLayout()
        title_label = QLabel(f"<span style='font-size: 15px; font-weight: 600;'>{name}</span>")
        header.addWidget(title_label)
        header.addStretch()
        self.visible_chk = QCheckBox("Visible")
        self.visible_chk.setChecked(True)
        header.addWidget(self.visible_chk)
        layout.addLayout(header)

        # Opacity Slider with label
        opacity_row = QHBoxLayout()
        opacity_label = QLabel("Opacity")
        opacity_label.setStyleSheet(f"color: {THEME['text_secondary']}; font-size: 12px;")
        self.opacity_value = QLabel("85%")
        self.opacity_value.setStyleSheet(f"color: {THEME['accent']}; font-size: 12px; font-weight: 600;")
        opacity_row.addWidget(opacity_label)
        opacity_row.addStretch()
        opacity_row.addWidget(self.opacity_value)
        layout.addLayout(opacity_row)
        
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(85)
        self.slider.valueChanged.connect(lambda v: self.opacity_value.setText(f"{v}%"))
        layout.addWidget(self.slider)

        # Color Picker Button
        self.color_btn = QPushButton("● Surface Color")
        self.color_btn.setObjectName("ColorBtn")
        self.color_btn.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {initial_color}, stop:1 {initial_color}dd);
            color: #000; 
            font-weight: 600;
            border-radius: 8px;
            padding: 10px;
        """)
        self.color_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.color_btn.clicked.connect(self.pick_color)
        layout.addWidget(self.color_btn)

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_btn.setStyleSheet(f"""
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {color.name()}, stop:1 {color.name()}dd);
                color: #000;
                font-weight: 600;
                border-radius: 8px;
                padding: 10px;
            """)

class MedicalWorkspace(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Analysis Suite")
        self.resize(1280, 900)
        self.setStyleSheet(STYLE_SHEET)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.init_selection_screen()

    def init_selection_screen(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        # Add stretch to push content to center
        layout.addStretch()

        # Header section
        header_container = QWidget()
        header_layout = QVBoxLayout(header_container)
        header_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_layout.setSpacing(8)

        title = QLabel("Select Target Anatomy")
        title.setObjectName("Title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(title)

        subtitle = QLabel("Choose an organ for AI-powered 3D segmentation analysis")
        subtitle.setObjectName("Subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_layout.addWidget(subtitle)


        layout.addWidget(header_container)
        layout.addSpacing(40)

        # Organ grid
        grid = QHBoxLayout()
        grid.setSpacing(50)

        self.organ_data = {
            "Liver": ["Right Lobe", "Left Lobe", "Gallbladder"],
            "Kidneys": ["Left Kidney", "Right Kidney", "Adrenal Glands"],
            "Stomach": ["Fundus", "Gastric Body", "Antrum"]
        }

        script_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(script_dir, "icons")

        for organ_name in self.organ_data.keys():
            container = QWidget()
            container_layout = QVBoxLayout(container)
            container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            container_layout.setSpacing(16)
            container_layout.setContentsMargins(0, 0, 0, 0)
            
            btn = QPushButton()
            btn.setObjectName("OrganButton")
            btn.setFixedSize(200, 200)  # Larger than icon for visible frame
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            add_shadow(btn, blur=30, offset=8, color=QColor(0, 0, 0, 100))
            
            image_path = os.path.join(images_dir, f"{organ_name.lower()}.jpeg")
            if os.path.exists(image_path):
                # Create rounded pixmap
                pixmap = QPixmap(image_path)
                pixmap = pixmap.scaled(160, 160, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
                
                # Create rounded mask
                rounded = QPixmap(160, 160)
                rounded.fill(Qt.GlobalColor.transparent)
                painter = QPainter(rounded)
                painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                path = QPainterPath()
                path.addRoundedRect(0, 0, 160, 160, 12, 12)  # 12px rounded corners
                painter.setClipPath(path)
                painter.drawPixmap(0, 0, pixmap)
                painter.end()
                
                btn.setIcon(QIcon(rounded))
                btn.setIconSize(QSize(160, 160))
            
            btn.clicked.connect(lambda ch, n=organ_name: self.open_analysis(n))
            container_layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
            
            label = QLabel(organ_name)
            label.setStyleSheet(f"""
                font-size: 20px; 
                font-weight: 600; 
                color: {THEME['text_primary']};
                letter-spacing: 0.5px;
            """)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            container_layout.addWidget(label)
            
            grid.addWidget(container)
        layout.addLayout(grid)
        
        # Add stretch to push content to center
        layout.addStretch()
        self.stack.addWidget(page)

    def open_analysis(self, organ_name):
        workspace = QWidget()
        layout = QHBoxLayout(workspace)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # --- LEFT PANEL ---
        left = QFrame()
        left.setObjectName("ControlCard")
        left.setFixedWidth(340)
        add_shadow(left, blur=20, offset=5)
        l_lay = QVBoxLayout(left)
        l_lay.setSpacing(16)
        
        # Header
        header = QLabel(f"<span style='font-size: 24px; font-weight: 700;'>{organ_name}</span><br/>"
                       f"<span style='font-size: 13px; color: {THEME['text_secondary']};'>Analysis Dashboard</span>")
        l_lay.addWidget(header)
        
        # Divider
        divider = QFrame()
        divider.setFixedHeight(1)
        divider.setStyleSheet(f"background: {THEME['glass_border']};")
        l_lay.addWidget(divider)
        
        # Model Selection
        model_label = QLabel("AI Segmentation Model")
        model_label.setStyleSheet(f"font-size: 13px; color: {THEME['text_secondary']}; font-weight: 500;")
        l_lay.addWidget(model_label)
        
        models = QComboBox()
        models.addItems(["Total Segmentator", "Swin UNETR", "MedSAM"])
        l_lay.addWidget(models)

        l_lay.addSpacing(10)
        
        # Metrics Section
        metrics_header = QLabel("Segmentation Metrics")
        metrics_header.setStyleSheet(f"font-size: 13px; color: {THEME['text_secondary']}; font-weight: 500;")
        l_lay.addWidget(metrics_header)
        
        metrics = QFrame()
        metrics.setObjectName("GlassCard")
        metrics.setStyleSheet(f"""
            background: rgba(15, 15, 40, 0.5);
            border-radius: 14px;
            border: 1px solid {THEME['glass_border']};
            padding: 14px;
        """)
        m_lay = QVBoxLayout(metrics)
        m_lay.setSpacing(12)
        
        # Fake metrics for demo
        import random
        dice = f"0.{random.randint(92, 98)}"
        iou = f"0.{random.randint(88, 94)}"
        hd95 = f"{random.randint(2, 8)}.4"
        
        # Metric items with icons
        for metric_name, metric_val, color in [
            ("Dice Score", dice, THEME['success']),
            ("Jaccard (IoU)", iou, THEME['success']),
            ("Hausdorff (HD95)", f"{hd95} mm", THEME['warning'])
        ]:
            row = QHBoxLayout()
            name = QLabel(metric_name)
            name.setStyleSheet(f"font-size: 13px; color: {THEME['text_secondary']};")
            val = QLabel(f"<b style='color: {color}; font-size: 15px;'>{metric_val}</b>")
            row.addWidget(name)
            row.addStretch()
            row.addWidget(val)
            m_lay.addLayout(row)
        
        l_lay.addWidget(metrics)

        l_lay.addStretch()
        
        back = QPushButton("← Back to Selection")
        back.setObjectName("BackButton")
        back.setCursor(Qt.CursorShape.PointingHandCursor)
        back.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        l_lay.addWidget(back)

        # --- CENTER PANEL ---
        center = QFrame()
        center.setObjectName("ControlCard")
        add_shadow(center, blur=20, offset=5)
        c_lay = QVBoxLayout(center)
        
        view_header = QLabel(f"<span style='font-size: 16px; font-weight: 600;'>3D Surface Extraction</span>")
        c_lay.addWidget(view_header, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # VTK 3D Viewer or placeholder
        if VTK_AVAILABLE:
            # Create a container for the viewer
            viewer_container = QWidget()
            viewer_layout = QVBoxLayout(viewer_container)
            viewer_layout.setContentsMargins(0, 0, 0, 0)
            c_lay.addWidget(viewer_container)
            
            # Temporary loading label
            loading_label = QLabel("Initializing 3D Analysis...\nPlease wait...")
            loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            loading_label.setStyleSheet(f"color: {THEME['text_secondary']}; font-size: 14px;")
            viewer_layout.addWidget(loading_label)
            
            # Define initialization function
            def init_vtk_viewer():
                try:
                    # Remove loading label
                    loading_label.setParent(None)
                    
                    # Create and add viewer
                    viewer_3d = VTK3DViewer(organ_name=organ_name)
                    viewer_layout.addWidget(viewer_3d)
                    
                    # --- AUTO LOADER ONLY ---
                    # Automatically load default asset if available
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    # Map organ GUI names to filenames
                    filename_map = {
                        "Liver": "liver.nii.gz",
                        "Kidneys": "kidney_right.nii.gz", # Default to right kidney
                        "Stomach": "stomach.nii.gz"
                    }
                    target_file = filename_map.get(organ_name)
                    
                    loaded = False
                    if target_file:
                        # Construct path: ../Assets/SwinUnter/[Organ]/[file]
                        asset_path = os.path.join(script_dir, "..", "Assets", "SwinUnter", organ_name, target_file)
                        asset_path = os.path.abspath(asset_path)
                        
                        if os.path.exists(asset_path):
                            print(f"Auto-loading asset: {asset_path}")
                            QApplication.processEvents()
                            viewer_3d.load_nifti(asset_path)
                            QApplication.processEvents()
                            viewer_3d.generate_hollow_3d(wall_thickness=2, opacity=0.7)
                            loaded = True
                        else:
                            print(f"Asset not found: {asset_path}")
                    
                    if not loaded:
                         # Show error in viewer if auto-load failed
                        err = QLabel(f"Data for {organ_name} unavailable.\nExpected at: {asset_path}")
                        err.setStyleSheet("color: #F87171; font-size: 14px;")
                        err.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        viewer_layout.addWidget(err)
                        viewer_3d.hide()

                except Exception as e:
                    print(f"Error initializing VTK: {e}")
                    label = QLabel(f"Error initializing 3D Engine:\n{str(e)}")
                    label.setStyleSheet("color: #F87171;")
                    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    viewer_layout.addWidget(label)

            # Schedule initialization after UI shows
            from PyQt6.QtCore import QTimer
            QTimer.singleShot(100, init_vtk_viewer)
            
        else:
            # Fallback placeholder if VTK not available
            placeholder = QFrame()
            placeholder.setStyleSheet(f"""
                border: 2px dashed rgba(108, 159, 255, 0.3);
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(10, 15, 26, 0.8),
                    stop:1 rgba(20, 25, 40, 0.8));
                border-radius: 12px;
            """)
            placeholder_layout = QVBoxLayout(placeholder)
            placeholder_label = QLabel("VTK not installed - 3D viewer unavailable\nInstall with: pip install vtk")
            placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            placeholder_label.setStyleSheet(f"color: {THEME['text_secondary']}; font-size: 14px;")
            placeholder_layout.addWidget(placeholder_label)
            c_lay.addWidget(placeholder)

        # --- RIGHT PANEL ---
        right_container = QWidget()
        right = QVBoxLayout(right_container)
        right.setSpacing(12)
        
        layers_header = QLabel("<span style='font-size: 16px; font-weight: 600;'>Visualization Layers</span>")
        right.addWidget(layers_header)
        
        part_colors = ["#FFB347", "#FF6B8A", "#4DD4AC"]
        for i, part_name in enumerate(self.organ_data[organ_name]):
            control = PartControl(part_name, part_colors[i])
            add_shadow(control, blur=15, offset=3)
            right.addWidget(control)
        
        right.addStretch()

        layout.addWidget(left)
        layout.addWidget(center, stretch=2)
        layout.addWidget(right_container)

        self.stack.addWidget(workspace)
        self.stack.setCurrentIndex(self.stack.count() - 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MedicalWorkspace()
    window.show()
    sys.exit(app.exec())