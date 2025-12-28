# 🏥 Medical Imaging Segmentation Suite
<img width="1581" height="976" alt="Screenshot 2025-12-28 191949" src="https://github.com/user-attachments/assets/29c31f74-6352-4596-8e24-6743dcce5997" />

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyQt6](https://img.shields.io/badge/PyQt6-6.0+-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![VTK](https://img.shields.io/badge/VTK-9.0+-E34F26?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

### *AI-Powered 3D Medical Image Analysis Platform*

**A cutting-edge desktop application for comparing and visualizing medical imaging segmentation results from multiple state-of-the-art AI models**

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#-documentation) • [🎯 Features](#-key-features) • [💻 Installation](#-installation)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Supported Models](#-supported-ai-models)
- [Supported Organs](#-supported-anatomical-structures)
- [Evaluation Metrics](#-evaluation-metrics)
- [Project Structure](#-project-structure)
- [Technical Architecture](#-technical-architecture)
- [Troubleshooting](#-troubleshooting)
- [Development](#-development--customization)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

### What is Medical Imaging Segmentation Suite?

The **Medical Imaging Segmentation Suite** is a professional-grade desktop application designed for medical imaging researchers, radiologists, and AI developers. It bridges the gap between complex AI segmentation models and practical clinical visualization.

### 🔬 Core Capabilities

**Workflow Pipeline:**
```
CT Scan → AI Segmentation → NIfTI Files → This Application → 3D Visualization + Metrics + Model Comparison
```

**Key Features:**

| Feature | Description |
|---------|-------------|
| 🤖 **AI Model Comparison** | Side-by-side evaluation of Swin UNETR, Total Segmentator, and WholeBody CT |
| 🎨 **Interactive 3D Visualization** | Real-time manipulation of organ structures with smooth rendering |
| 📊 **Quantitative Analysis** | Dice Score, IoU, and Hausdorff Distance metrics |
| 🔧 **Customizable Views** | Individual control over opacity, color, and visibility of each structure |
| 🚀 **High Performance** | Automatic optimization for large datasets |
| 💎 **Modern UI** | Premium glassmorphism design with intuitive controls |

---

## ✨ Key Features

### 🎨 Modern Glassmorphic Interface

- Premium dark theme with frosted glass effects
- Smooth animations and hover interactions
- Responsive three-panel workspace layout
- Hardware-accelerated rendering

### 🔬 Advanced 3D Visualization

- Multi-part organ rendering
- Real-time property adjustments
- Professional surface extraction
- Cinematic lighting and shadows

### 📊 Comprehensive Metrics

- **Dice Coefficient**: Overlap accuracy
- **IoU (Jaccard Index)**: Intersection metric
- **Hausdorff Distance**: Boundary precision
- Real-time updates when switching models

### 🎯 Intuitive Controls

- Layer-based visibility toggles
- Smooth opacity sliders (0-100%)
- Custom color pickers
- Model switching with one click

---

## 🚀 Quick Start

Get up and running in **5 minutes**:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/medical-segmentation-suite.git
cd medical-segmentation-suite

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
cd gui
python gui.py
```

**That's it!** 🎉 The application window will open with the organ selection screen.

---

## 💻 Installation

### Prerequisites

| Requirement | Version | Status |
|------------|---------|--------|
| Python | 3.8+ | ✅ Required |
| pip | Latest | ✅ Required |
| RAM | 4GB+ | ⚠️ Recommended 8GB |
| Graphics | OpenGL Support | ✅ For 3D rendering |

### Step-by-Step Installation

**Windows:**

```bash
# 1. Install Python from python.org
# Make sure to check "Add Python to PATH"

# 2. Verify installation
python --version

# 3. Clone repository
git clone https://github.com/yourusername/medical-segmentation-suite.git
cd medical-segmentation-suite

# 4. Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run application
cd gui
python gui.py
```

**macOS:**

```bash
# 1. Install Python using Homebrew
brew install python@3.11

# 2. Verify installation
python3 --version

# 3. Clone repository
git clone https://github.com/yourusername/medical-segmentation-suite.git
cd medical-segmentation-suite

# 4. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run application
cd gui
python gui.py
```

**Linux (Ubuntu/Debian):**

```bash
# 1. Install Python and dependencies
sudo apt update
sudo apt install python3 python3-pip python3-venv

# 2. Clone repository
git clone https://github.com/yourusername/medical-segmentation-suite.git
cd medical-segmentation-suite

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run application
cd gui
python gui.py
```

### Dependencies

Create a `requirements.txt` file:

```txt
PyQt6>=6.0.0
vtk>=9.0.0
SimpleITK>=2.0.0
numpy>=1.20.0
pandas>=1.3.0
```

### Verify Installation

```bash
# Test all dependencies
python -c "import PyQt6, vtk, SimpleITK, numpy, pandas; print('✅ All dependencies installed successfully!')"
```

---

## 📖 Usage Guide

### Application Workflow

```
Launch Application 
    ↓
Organ Selection Screen
    ↓
Choose Organ (Liver/Kidneys/Stomach)
    ↓
Analysis Workspace
    ├── View 3D Model
    ├── Check Metrics
    └── Adjust Controls
         ↓
    Switch Model? → Select New Model → Back to 3D Model
         ↓
    Continue Analysis
         ↓
    Back to Selection
```

### 1️⃣ Organ Selection Screen

**Available Organs:**

| Organ | Structures | Description |
|-------|------------|-------------|
| 🔴 **Liver System** | 4 structures | Liver, Gallbladder, Spleen, Portal/Splenic Vein |
| 🟤 **Kidney System** | 6 structures | Left/Right Kidneys, Adrenal Glands, Aorta, IVC |
| 🟢 **Stomach System** | 3 structures | Stomach, Pancreas, Esophagus |

**How to Use:**
- Click any organ button to enter the analysis workspace
- Application loads all segmentation data automatically

---

### 2️⃣ Analysis Workspace

The workspace is divided into **three panels**:

```
┌──────────────┬─────────────────────────┬──────────────┐
│              │                         │              │
│  Left Panel  │    Center Panel         │ Right Panel  │
│  (Controls)  │    (3D Viewer)          │  (Layers)    │
│              │                         │              │
└──────────────┴─────────────────────────┴──────────────┘
```

#### 📊 Left Panel: Control Dashboard

```
┌─────────────────────────────────┐
│ Liver                           │
│ Analysis Dashboard              │
├─────────────────────────────────┤
│                                 │
│ 🤖 AI Segmentation Model        │
│ ┌─────────────────────────────┐ │
│ │ Swin UNETR              ▼  │ │
│ └─────────────────────────────┘ │
│                                 │
│ 📊 Segmentation Metrics         │
│ ┌─────────────────────────────┐ │
│ │ Dice Score       0.9234     │ │
│ │ Jaccard (IoU)    0.8567     │ │
│ │ Hausdorff        3.45 mm    │ │
│ └─────────────────────────────┘ │
│                                 │
│ ┌─────────────────────────────┐ │
│ │  ← Back to Selection        │ │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘
```

**Features:**
- 🔄 **Model Selection**: Switch between AI models
- 📈 **Live Metrics**: Real-time performance indicators
- 🔙 **Navigation**: Return to organ selection

#### 🎨 Center Panel: 3D Visualization

**Mouse Controls:**

| Action | Control |
|--------|---------|
| 🔄 Rotate | Left-click + Drag |
| 🔍 Zoom | Mouse Wheel / Right-click + Drag |
| 🖐️ Pan | Middle-click + Drag |

**Rendering Features:**
- ✨ Smooth surface extraction using Marching Cubes
- 🌟 Professional lighting with specular highlights
- 🎭 Semi-transparent rendering for internal structures
- 🎬 Hardware-accelerated graphics

#### 🎛️ Right Panel: Visualization Layers

Each anatomical structure has independent controls:

```
┌────────────────────────────────┐
│ 🔴 Liver              ☑ Visible │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ Opacity                    70%  │
│ ├═══════════○──────────────┤   │
│ ┌──────────────────────────┐   │
│ │    ● Surface Color       │   │
│ └──────────────────────────┘   │
└────────────────────────────────┘
```

**Controls:**
- ✅ **Visibility Checkbox**: Show/hide structure
- 🎚️ **Opacity Slider**: Adjust transparency (0-100%)
- 🎨 **Color Picker**: Customize surface color

**Use Cases:**
- Hide outer organs to see internal structures
- Make liver semi-transparent to view vessels
- Color-code similar structures for clarity

---

### 3️⃣ Practical Examples

**Example 1: Examining Gallbladder Position**

Goal: View the gallbladder location relative to the liver

Steps:
1. Click **Liver** on the selection screen
2. In the 3D view, rotate to anterior view
3. Find **Liver** in the right panel
4. Adjust opacity slider to **40%**
5. The gallbladder is now visible inside!
6. Click **Gallbladder color button**
7. Choose **bright yellow** for contrast
8. Rotate to examine from multiple angles

Result: Clear visualization of gallbladder-liver relationship! ✨

---

**Example 2: Comparing Model Accuracy**

Goal: Determine which model segments kidneys best

Steps:
1. Click **Kidneys** on the selection screen
2. Note the current metrics (Swin UNETR):
   - Dice: 0.8956
   - IoU: 0.8123
   - HD95: 4.78 mm
3. Switch to **Total Segmentator** in dropdown
4. Compare new metrics:
   - Dice: 0.9012
   - IoU: 0.8234
   - HD95: 3.89 mm
5. Visually inspect 3D models for differences

Result: Total Segmentator shows slightly better metrics! 📊

---

**Example 3: Creating Custom Visualization**

Goal: Create a presentation-ready view

Steps:
1. Select desired organ
2. For each structure in right panel:
   - Adjust opacity for depth perception
   - Choose distinct colors (e.g., warm colors for organs, cool for vessels)
3. Rotate 3D view to optimal angle
4. Take a screenshot (future feature)

Result: Professional medical visualization ready for presentations! 🎬

---

## 🤖 Supported AI Models

### Model Comparison Matrix

| Feature | Swin UNETR | Total Segmentator | WholeBody CT |
|---------|------------|-------------------|--------------|
| **Architecture** | Vision Transformer | CNN-based | Hybrid |
| **Accuracy** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Speed** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Organs Supported** | ~25 | 104+ | ~40 |
| **GPU Required** | ✅ Yes | ⚠️ Optional | ⚠️ Optional |
| **Best For** | Research | Clinical | General Purpose |
| **File Prefix** | None | `ct_` | None |

---

### 1. Swin UNETR (Default)

**Full Name**: Swin Transformer U-Net with Transformers

**Architecture**: Vision Transformer-based segmentation

**Strengths:**
- State-of-the-art accuracy for complex organ boundaries
- Excellent generalization across different scan protocols
- Superior performance on small structures

**When to Use**: 
- High-precision medical research applications
- When computational resources are available
- For challenging segmentation tasks

**File Location**: `Assets/SwinUnter/[OrganName]/`  
**File Naming**: Standard names (e.g., `liver.nii.gz`)

**Performance Characteristics:**
- Training: Requires GPU
- Inference: GPU recommended
- Processing Time: ~30-60 seconds per organ

---

### 2. Total Segmentator

**Full Name**: TotalSegmentator v2

**Architecture**: Comprehensive CNN-based multi-organ segmentation

**Strengths:**
- Segments 104+ anatomical structures
- Very fast inference time
- Robust to different imaging protocols
- Works well without GPU

**When to Use**:
- Whole-body analysis requirements
- Clinical workflows needing speed
- Limited computational resources

**File Location**: `Assets/Total-Segmentator/[OrganName]/`  
**File Naming**: Prefix with `ct_` (e.g., `ct_liver.nii.gz`)

**Performance Characteristics:**
- Training: CPU/GPU compatible
- Inference: CPU sufficient
- Processing Time: ~10-20 seconds per organ

---

### 3. WholeBody CT

**Full Name**: WholeBody CT Segmentation

**Architecture**: Hybrid model for full-body CT scans

**Strengths:**
- Designed for complete torso scans
- Handles low-quality and varied contrast images
- Good balance between speed and accuracy

**When to Use**:
- Full-body scan analysis
- Varied image quality scenarios
- General-purpose segmentation

**File Location**: `Assets/WholeBodyCt/[OrganName]/`  
**File Naming**: Standard names (e.g., `liver.nii.gz`)

**Performance Characteristics:**
- Training: GPU recommended
- Inference: CPU/GPU flexible
- Processing Time: ~20-40 seconds per organ

---

## 🫀 Supported Anatomical Structures

### 🔴 Liver System

**Main Structures:**

1. **Liver**
   - Largest internal organ
   - Function: Detoxification, metabolism, bile production
   - Color: Red-brown

2. **Gallbladder**
   - Stores and concentrates bile
   - Small pear-shaped organ
   - Located inferior to liver

3. **Spleen**
   - Part of lymphatic system
   - Function: Blood filtration, immune response
   - Located in left upper abdomen

4. **Portal Vein and Splenic Vein**
   - Major hepatic blood vessels
   - Transport nutrient-rich blood to liver
   - Critical for hepatic circulation

**Segmentation Files:**

Swin UNETR / WholeBody CT:
```
liver.nii.gz
gallbladder.nii.gz
spleen.nii.gz
portal_vein_and_splenic_vein.nii.gz
```

Total Segmentator:
```
ct_liver.nii.gz
ct_gallbladder.nii.gz
ct_spleen.nii.gz
ct_portal_vein_and_splenic_vein.nii.gz
```

---

### 🟤 Kidney System

**Main Structures:**

1. **Left Kidney & Right Kidney**
   - Bean-shaped organs in retroperitoneum
   - Function: Blood filtration, urine production
   - Regulate fluid and electrolyte balance

2. **Left Adrenal Gland & Right Adrenal Gland**
   - Endocrine glands
   - Produce: Adrenaline, cortisol, aldosterone
   - Small triangular glands superior to kidneys

3. **Aorta**
   - Main artery from heart
   - Largest blood vessel in body
   - Supplies oxygenated blood to entire body

4. **Inferior Vena Cava (IVC)**
   - Main vein returning to heart
   - Collects deoxygenated blood
   - Runs parallel to aorta

**Segmentation Files:**

```
kidney_left.nii.gz
kidney_right.nii.gz
adrenal_gland_left.nii.gz
adrenal_gland_right.nii.gz
aorta.nii.gz
inferior_vena_cava.nii.gz
```

(Total Segmentator: Add `ct_` prefix)

---

### 🟢 Stomach System

**Main Structures:**

1. **Stomach**
   - J-shaped digestive organ
   - Function: Food digestion via acid and enzymes
   - Located in upper left abdomen

2. **Pancreas**
   - Dual-function gland (endocrine + exocrine)
   - Produces: Insulin, glucagon, digestive enzymes
   - Elongated organ posterior to stomach

3. **Esophagus**
   - Muscular tube connecting pharynx to stomach
   - Function: Food transport via peristalsis
   - Runs through thoracic cavity

**Segmentation Files:**

```
stomach.nii.gz
pancreas.nii.gz
esophagus.nii.gz
```

(Total Segmentator: Add `ct_` prefix)

---

## 📊 Evaluation Metrics

### Understanding Segmentation Quality

When AI models segment medical images, we need objective metrics to measure accuracy. These metrics compare the **AI prediction** against **ground truth** (expert-labeled reference).

---

### 1. 🎯 Dice Score (Dice Coefficient)

**What It Measures**: Overlap similarity between prediction and ground truth

**Formula:**
```
Dice = 2 × |Intersection| / (|Prediction| + |Ground Truth|)
Dice = 2 × |A ∩ B| / (|A| + |B|)
```

**Visual Explanation:**
```
AI Prediction:    [████]
Ground Truth:     [████]
Intersection:     [██]

Dice = 2 × 2 / (4 + 4) = 0.5 (50%)
```

**Range**: 0.0 to 1.0
- **0.0** = No overlap (completely wrong)
- **0.5** = 50% overlap (poor)
- **0.8** = 80% overlap (good)
- **0.9+** = 90%+ overlap (excellent)

**Interpretation Guidelines:**

| Score Range | Quality | Use Case |
|-------------|---------|----------|
| **0.90 - 1.00** | Excellent | Clinical-grade, ready for deployment |
| **0.80 - 0.90** | Good | Acceptable for research |
| **0.70 - 0.80** | Moderate | Needs improvement |
| **< 0.70** | Poor | Unacceptable, retrain model |

**Example:**
```
Dice Score: 0.9234
Meaning: The AI correctly identified 92.34% of the liver tissue overlap
```

---

### 2. 📐 IoU / Jaccard Index

**What It Measures**: Intersection over Union ratio

**Formula:**
```
IoU = |Intersection| / |Union|
IoU = |A ∩ B| / |A ∪ B|
```

**Visual Explanation:**
```
AI Prediction: [████]    Ground Truth: [████]
Union: [██████]    Intersection: [██]
IoU = 2 / 6 = 0.333 (33.3%)
```

**Range**: 0.0 to 1.0
- **0.0** = No overlap
- **0.5** = Moderate overlap
- **0.7+** = Good overlap
- **0.8+** = Excellent

**Relationship to Dice:**
```
IoU is always ≤ Dice Score
IoU = Dice / (2 - Dice)
Dice = 2 × IoU / (1 + IoU)
```

**Interpretation Guidelines:**

| Score Range | Quality | Description |
|-------------|---------|-------------|
| **> 0.80** | Excellent | High precision and recall |
| **0.70 - 0.80** | Good | Acceptable performance |
| **0.60 - 0.70** | Moderate | Borderline acceptable |
| **< 0.60** | Poor | Needs significant improvement |

**Example:**
```
IoU: 0.8567
Meaning: 85.67% of the combined predicted + actual area overlaps correctly
```

---

### 3. 📏 Hausdorff Distance (HD95)

**What It Measures**: Maximum distance between segmentation boundaries (95th percentile)

**Why 95th Percentile?**
- Ignores outliers (e.g., single misplaced pixel)
- More robust than absolute maximum distance
- Clinically relevant boundary accuracy

**Visual Explanation:**
```
AI Boundary:        ╱─────╲
Ground Truth:      ╱───────╲
                   ↕ = 3.45mm
```

**Units**: Millimeters (mm)

**Interpretation Guidelines:**

| Distance | Quality | Clinical Use |
|----------|---------|--------------|
| **< 2.0 mm** | Excellent | Suitable for surgery planning |
| **2.0 - 5.0 mm** | Good | Acceptable for most clinical applications |
| **5.0 - 10.0 mm** | Moderate | Borderline for clinical use |
| **> 10.0 mm** | Poor | Unacceptable boundary delineation |

**Why It Matters:**
- **Critical for**: Radiation therapy planning
- **Important for**: Surgical navigation systems
- **Measures**: How "tight" the segmentation boundary is

**Example:**
```
Hausdorff95: 3.45 mm
Meaning: 95% of boundary points are within 3.45mm of the true boundary
Good quality for most clinical applications
```

---

### Metrics Summary Table

| Metric | Type | Best Value | Units | What It Tells You |
|--------|------|-----------|-------|-------------------|
| **Dice** | Overlap | 1.0 (100%) | Dimensionless | Overall segmentation quality |
| **IoU** | Overlap | 1.0 (100%) | Dimensionless | Intersection proportion |
| **HD95** | Distance | 0.0 mm | Millimeters | Boundary precision |

---

### Real-World Example Comparison

**Scenario**: Comparing three models for liver segmentation

**Model 1: Swin UNETR**
```
Dice: 0.9234    → Excellent! 92.34% overlap
IoU: 0.8567     → Very good intersection
HD95: 3.45 mm   → Good boundary precision
Overall: Best choice for high-precision applications
```

**Model 2: Total Segmentator**
```
Dice: 0.8956    → Good, slightly lower
IoU: 0.8123     → Good intersection
HD95: 4.78 mm   → Acceptable boundary
Overall: Good balance of speed and accuracy
```

**Model 3: WholeBody CT**
```
Dice: 0.9012    → Good performance
IoU: 0.8234     → Good intersection
HD95: 3.89 mm   → Good boundary
Overall: Solid general-purpose choice
```

**Conclusion**: Swin UNETR performs best for this liver segmentation task, but Total Segmentator might be preferred if speed is critical.

---

## 📁 Project Structure

### Complete Directory Tree

```
medical-segmentation-suite/
│
├── gui/                                    # Application source code
│   ├── gui.py                             # Main application (1057 lines)
│   │   ├── MedicalWorkspace               # Main window controller
│   │   ├── PartControl                    # Layer control widgets
│   │   ├── add_shadow()                   # Visual effects
│   │   └── add_glow()                     # Glow effects
│   │
│   ├── viewer_3d.py                       # 3D visualization engine (338 lines)
│   │   └── VTK3DViewer                    # VTK rendering wrapper
│   │       ├── load_nifti()               # Load NIfTI files
│   │       ├── add_part_from_nifti()      # Add organ part
│   │       ├── set_part_opacity()         # Control transparency
│   │       ├── set_part_color()           # Change colors
│   │       └── set_part_visibility()      # Show/hide parts
│   │
│   └── icons/                             # Organ selection icons
│       ├── liver.jpeg                     # 512x512 recommended
│       ├── kidneys.jpeg
│       └── stomach.jpeg
│
├── Assets/                                # Segmentation data (NIfTI files)
│   │
│   ├── SwinUnter/                         # Swin UNETR model results
│   │   ├── Liver/
│   │   │   ├── liver.nii.gz
│   │   │   ├── gallbladder.nii.gz
│   │   │   ├── spleen.nii.gz
│   │   │   └── portal_vein_and_splenic_vein.nii.gz
│   │   │
│   │   ├── Kidneys/
│   │   │   ├── kidney_left.nii.gz
│   │   │   ├── kidney_right.nii.gz
│   │   │   ├── adrenal_gland_left.nii.gz
│   │   │   ├── adrenal_gland_right.nii.gz
│   │   │   ├── aorta.nii.gz
│   │   │   └── inferior_vena_cava.nii.gz
│   │   │
│   │   └── Stomach/
│   │       ├── stomach.nii.gz
│   │       ├── pancreas.nii.gz
│   │       └── esophagus.nii.gz
│   │
│   ├── Total-Segmentator/                # Total Segmentator results
│   │   ├── Liver/
│   │   │   ├── ct_liver.nii.gz           # Note: "ct_" prefix
│   │   │   ├── ct_gallbladder.nii.gz
│   │   │   ├── ct_spleen.nii.gz
│   │   │   └── ct_portal_vein_and_splenic_vein.nii.gz
│   │   │
│   │   ├── Kidneys/
│   │   │   └── [ct_*.nii.gz files]
│   │   │
│   │   └── Stomach/
│   │       └── [ct_*.nii.gz files]
│   │
│   └── WholeBodyCt/                      # WholeBody CT results
│       ├── Liver/
│       │   └── [*.nii.gz files]
│       ├── Kidneys/
│       │   └── [*.nii.gz files]
│       └── Stomach/
│           └── [*.nii.gz files]
│
├── Evaluation-Metrics/                    # CSV files with metrics
│   ├── TotalSegmentator_summary.csv
│   ├── SwinUnter_summary.csv
│   └── WholeBodyCt_summary.csv
│
├── docs/                                  # Documentation (optional)
│   ├── preview.png
│   └── screenshots/
│
├── requirements.txt                       # Python dependencies
├── README.md                              # This file
├── LICENSE                                # MIT License
└── .gitignore                            # Git ignore file
```

---

### File Descriptions

**Core Application Files:**

| File | Size | Description |
|------|------|-------------|
| `gui/gui.py` | ~1057 lines | Main application window, UI logic, state management |
| `gui/viewer_3d.py` | ~338 lines | VTK 3D rendering engine, surface extraction |
| `gui/icons/*.jpeg` | < 100 KB each | Organ selection button images |

**Data Files:**

| File Type | Location | Purpose |
|-----------|----------|---------|
| `.nii.gz` | `Assets/*/` | Segmented organ volumes (NIfTI format) |
| `.csv` | `Evaluation-Metrics/` | Performance metrics per model/organ |

**Configuration Files:**

| File | Purpose |
|------|---------|
| `requirements.txt` | Python package dependencies |
| `README.md` | Complete documentation (this file) |
| `LICENSE` | MIT license text |

---

### CSV File Format

**Structure of Metrics CSV:**

```csv
Organ,Dice,IoU,Hausdorff95
Liver,0.9234,0.8567,3.45
Kidneys,0.8956,0.8123,4.78
Stomach,0.9012,0.8234,3.89
```

**Column Requirements:**
- `Organ`: Must match organ names exactly (case-sensitive)
- `Dice`: Float 0.0-1.0 (overlap metric)
- `IoU`: Float 0.0-1.0 (intersection metric)
- `Hausdorff95`: Float in millimeters (boundary metric)

**Important Notes:**
- Column names must be exact: `Organ`, `Dice`, `IoU`, `Hausdorff95`
- Use comma delimiter
- Include header row
- Organ names must match code exactly

---

### File Naming Conventions

**Swin UNETR & WholeBody CT:**
```
Format: [organ_name].nii.gz

Examples:
  liver.nii.gz
  kidney_left.nii.gz
  adrenal_gland_right.nii.gz
  portal_vein_and_splenic_vein.nii.gz
```

**Total Segmentator:**
```
Format: ct_[organ_name].nii.gz

Examples:
  ct_liver.nii.gz
  ct_kidney_left.nii.gz
  ct_adrenal_gland_right.nii.gz
  ct_portal_vein_and_splenic_vein.nii.gz
```

**Why Different Naming?**
- Total Segmentator uses `ct_` prefix by convention
- Application automatically handles this via `MODEL_FILE_PREFIX` dictionary
- No manual renaming required

---

## 🔧 Technical Architecture

### Application Flow Diagram

```
┌─────────────────────────────────────────┐
│     User Opens Application              │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│   Initialize MedicalWorkspace           │
│   - Load all metrics CSV files          │
│   - Apply glassmorphism theme           │
│   - Create organ selection screen       │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│   User Selects Organ (e.g., Liver)     │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│    Create Analysis Workspace            │
│    - Build left panel (controls)        │
│    - Initialize VTK3DViewer             │
│    - Create right panel (layers)        │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│      Load Model Data (async)            │
│      For each organ part:               │
│      1. Read NIfTI with SimpleITK       │
│      2. Convert to NumPy array          │
│      3. Pass to VTK3DViewer             │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│     VTK 3D Rendering Pipeline           │
│     1. Convert NumPy → VTK ImageData    │
│     2. Apply Marching Cubes             │
│     3. Smooth with Windowed Sinc        │
│     4. Create Actor (color/opacity)     │
│     5. Add to renderer                  │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│       User Interactions                 │
│       - Rotate/zoom 3D view             │
│       - Adjust opacity → Update actors  │
│       - Toggle visibility               │
│       - Change colors                   │
│       - Switch models → Reload pipeline │
└─────────────────────────────────────────┘
```

---

### Core Components

**1. MedicalWorkspace Class** (`gui.py`)

Purpose: Main application controller

Key Methods:
```python
__init__()                  # Initialize app, load metrics
init_selection_screen()     # Create organ selection UI
open_analysis(organ_name)   # Build analysis workspace
load_model_data()           # Load NIfTI files for selected model
on_model_changed()          # Handle model dropdown changes
refresh_layer_controls()    # Rebuild right panel
update_metrics_display()    # Update metric labels
```

State Variables:
```python
self.current_organ         # "Liver", "Kidneys", or "Stomach"
self.current_model         # Selected AI model name
self.viewer_3d             # Reference to VTK3DViewer
self.metrics_data          # All loaded metrics
self.part_controls         # List of PartControl widgets
```

---

**2. VTK3DViewer Class** (`viewer_3d.py`)

Purpose: Handle all 3D visualization using VTK

Key Methods:
```python
load_nifti(file_path)              # Load single NIfTI file
add_part_from_nifti(path, name)    # Load and render organ part
set_part_opacity(name, value)      # Change transparency
set_part_color(name, rgb)          # Change surface color
set_part_visibility(name, bool)    # Show/hide part
reset_viewer()                     # Clear all actors
```

VTK Pipeline:
```
vtkImageData (volume) 
    ↓
vtkDiscreteMarchingCubes (surface extraction)
    ↓
vtkWindowedSincPolyDataFilter (smoothing)
    ↓
vtkPolyDataMapper (geometry mapping)
    ↓
vtkActor (renderable object)
    ↓
vtkRenderer (scene display)
```

---

**3. PartControl Class** (`gui.py`)

Purpose: UI widget for controlling one anatomical part

Components:
```python
self.visible_chk       # QCheckBox - show/hide
self.slider           # QSlider - opacity 0-100%
self.color_btn        # QPushButton - color picker
self.viewer_3d        # Reference to VTK viewer
```

Signal Connections:
```python
visible_chk.toggled → viewer_3d.set_part_visibility()
slider.valueChanged → viewer_3d.set_part_opacity()
color_btn.clicked → pick_color() → viewer_3d.set_part_color()
```

---

### Data Processing Pipeline

**Step 1: NIfTI File Loading**

```python
img = sitk.ReadImage("liver.nii.gz")
img = sitk.DICOMOrient(img, 'LPS')  # Standardize orientation
np_data = sitk.GetArrayFromImage(img)
spacing = img.GetSpacing()
```

What Happens:
- File read from disk
- Image reoriented to standard LPS coordinate system
- 3D volume → NumPy array (e.g., `[512, 512, 300]`)
- Voxel spacing extracted (e.g., `[0.5mm, 0.5mm, 1.0mm]`)

---

**Step 2: Downsampling (if needed)**

```python
if max(np_data.shape) > 256:
    np_data = np_data[::2, ::2, ::2]
    spacing = tuple(s * 2 for s in spacing)
```

Why: Prevents freezing on large files (>256³ voxels)

---

**Step 3: Convert to VTK Format**

```python
# Permute from Z,Y,X to X,Y,Z
data_perm = np.transpose(np_data, (2, 1, 0))
flat_data = data_perm.flatten(order='F')

# Create VTK array
vtk_array = numpy_support.numpy_to_vtk(flat_data)

# Create VTK image
img_data = vtk.vtkImageData()
img_data.SetDimensions(width, height, depth)
img_data.SetSpacing(spacing)
img_data.GetPointData().SetScalars(vtk_array)
```

---

**Step 4: Surface Extraction (Marching Cubes)**

```python
mc = vtk.vtkDiscreteMarchingCubes()
mc.SetInputData(img_data)
mc.GenerateValues(1, target_label, target_label)
```

What It Does:
- Finds boundary between labeled and unlabeled voxels
- Creates triangular mesh of the surface
- Output: 3D polygon mesh

---

**Step 5: Surface Smoothing**

```python
smoother = vtk.vtkWindowedSincPolyDataFilter()
smoother.SetInputConnection(mc.GetOutputPort())
smoother.SetNumberOfIterations(15)
smoother.SetPassBand(0.001)
```

Why Smooth:
- Raw Marching Cubes output is blocky
- Smoothing creates natural organic surfaces
- Professional medical visualization quality

---

**Step 6: Rendering**

```python
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(smoother.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(color)
actor.GetProperty().SetOpacity(opacity)

renderer.AddActor(actor)
```

Result: Smooth, colored 3D organ appears! ✨

---

### Performance Optimizations

**1. Asynchronous Loading**
```python
QTimer.singleShot(100, init_vtk_viewer)
```
- Delays 3D initialization by 100ms
- UI remains responsive

**2. Automatic Downsampling**
- Files >256³ voxels reduced by 50%
- Maintains visual quality

**3. Efficient Data Structures**
```python
self.actors = {}  # O(1) lookup
```

**4. Progressive Rendering**
```python
QApplication.processEvents()  # UI updates during loading
```

---

## 🔍 Troubleshooting

### Problem 1: Application Won't Start

**Symptom:** Error when running `python gui.py`

**Solutions:**

```bash
# Check Python version
python --version  # Should be 3.8+

# Install dependencies
pip install -r requirements.txt

# Verify you're in correct directory
pwd  # Should be in .../gui/ folder
cd gui

# Check for import errors
python -c "import PyQt6, vtk, SimpleITK"
```

---

### Problem 2: VTK Not Available

**Symptom:** "VTK not available - 3D viewer will be disabled"

**Solution:**
```bash
pip install vtk

# If that fails:
pip install vtk==9.2.6

# macOS: May need Xcode Command Line Tools
xcode-select --install

# Linux: May need OpenGL libraries
sudo apt install libgl1-mesa-dev
```

---

### Problem 3: Blank 3D Viewport

**Symptom:** Dark background, no 3D model

**Possible Causes:**

1. **NIfTI files missing**
   ```bash
   # Check files exist
   ls Assets/SwinUnter/Liver/
   ```

2. **Empty segmentation files**
   - Check console for: "No label found in [file]"
   - Solution: Use valid segmentation files

3. **Graphics driver issue**
   - Update graphics drivers
   - Verify OpenGL support

---

### Problem 4: Application Freezes

**Symptom:** App stops responding during loading

**Causes & Solutions:**

- **Large NIfTI files**: Wait 30-60 seconds (auto-downsampled)
- **Insufficient RAM**: Close other applications
- **Many parts loading**: Be patient, processing takes time

---

### Problem 5: Metrics Show 0.0000

**Symptom:** All metrics display as 0.0000

**Solutions:**

1. **Check CSV files exist**
   ```bash
   ls Evaluation-Metrics/
   ```

2. **Verify organ names match exactly**
   ```
   ✓ Liver
   ✗ liver
   ✗ LIVER
   ```

3. **Check CSV format**
   ```csv
   Organ,Dice,IoU,Hausdorff95
   Liver,0.9234,0.8567,3.45
   ```

---

### Problem 6: Colors Not Changing

**Solution:**
- Ensure `connect_part_controls()` is called after `load_model_data()`
- Check console for connection errors

---

### Problem 7: Icons Not Showing

**Symptom:** Organ buttons have no images

**Solutions:**

```bash
# Check files exist
ls gui/icons/

# Must be JPEG format
# Correct: liver.jpeg
# Wrong: liver.png, Liver.jpeg
```

---

## 🛠️ Development & Customization

### Adding New Organs

**Step 1:** Update `organ_data` dictionary

```python
self.organ_data = {
    "Heart": {
        "Swin UNETR": [
            ("heart.nii.gz", "Heart"),
            ("aorta.nii.gz", "Aorta"),
            ("pulmonary_artery.nii.gz", "Pulmonary Artery")
        ],
        "Total Segmentator": [
            ("ct_heart.nii.gz", "Heart"),
            ("ct_aorta.nii.gz", "Aorta"),
            ("ct_pulmonary_artery.nii.gz", "Pulmonary Artery")
        ]
    }
}
```

**Step 2:** Add icon
```bash
# Place image at: gui/icons/heart.jpeg
# Recommended size: 512x512 pixels
```

**Step 3:** Create directories
```bash
mkdir -p Assets/SwinUnter/Heart
mkdir -p Assets/Total-Segmentator/Heart
```

**Step 4:** Add metrics to CSV
```csv
Heart,0.9156,0.8445,2.89
```

Done! Application automatically recognizes the new organ.

---

### Customizing the Theme

**Change Background Gradient:**

```python
THEME = {
    "bg_mesh_1": "#YOUR_COLOR_1",  # Top-left
    "bg_mesh_2": "#YOUR_COLOR_2",  # Top-right
    "bg_mesh_3": "#YOUR_COLOR_3",  # Bottom-left
    "bg_mesh_4": "#YOUR_COLOR_4",  # Bottom-right
}
```

**Change Accent Color:**

```python
THEME = {
    "accent": "#FF6B6B",        # Red accent
    "accent_bright": "#FF8787",
    "accent_deep": "#FF4D4D",
}
```

**Change Glass Transparency:**

```python
THEME = {
    "glass_bg": "rgba(15, 15, 35, 0.8)",  # More opaque
}
```

---

### Adding New Features

**Feature: Export to STL**

```python
# In VTK3DViewer class:
def export_to_stl(self, filename):
    """Export 3D model to STL file."""
    if not self.actors:
        return False
    
    writer = vtk.vtkSTLWriter()
    writer.SetFileName(filename)
    
    append = vtk.vtkAppendPolyData()
    for actor in self.actors.values():
        append.AddInputData(actor.GetMapper().GetInput())
    append.Update()
    
    writer.SetInputData(append.GetOutput())
    writer.Write()
    return True
```

**Feature: Screenshot Capture**

```python
# In VTK3DViewer class:
def capture_screenshot(self, filename):
    """Save current view as PNG."""
    w2if = vtk.vtkWindowToImageFilter()
    w2if.SetInput(self.vtkWidget.GetRenderWindow())
    w2if.Update()
    
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(filename)
    writer.SetInputConnection(w2if.GetOutputPort())
    writer.Write()
```

**Feature: Auto-Rotation**

```python
# In VTK3DViewer class:
def start_auto_rotation(self):
    """Automatically rotate view."""
    self.timer = QTimer()
    self.timer.timeout.connect(self.rotate_step)
    self.timer.start(50)  # 20 FPS

def rotate_step(self):
    """Rotate camera one step."""
    camera = self.renderer.GetActiveCamera()
    camera.Azimuth(2)
    self.vtkWidget.GetRenderWindow().Render()
```

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Contribution Process

1. **Fork the repository**
2. **Create feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly**
   - Run application
   - Test all organs
   - Test all models
5. **Commit changes**
   ```bash
   git commit -m "Add: Feature description"
   ```
6. **Push to fork**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open Pull Request**

---

### Contribution Ideas

- 🎨 Add more organ types (heart, lungs, brain)
- 📊 Implement additional metrics (Sensitivity, Specificity)
- 🎬 Animation and rotation features
- 📷 Screenshot and export functionality
- 🎨 Additional color themes
- 🌐 Multi-language support
- 📝 Annotation tools
- 🔊 Accessibility features
- 📖 Video tutorials
- 🧪 Unit tests

---

### Code Style Guidelines

**Naming Conventions:**
```python
ClassName           # Classes: CapitalizedWords
function_name       # Functions: lowercase_with_underscores
CONSTANT_NAME       # Constants: ALL_CAPS
variable_name       # Variables: lowercase
```

**Documentation:**
```python
def function(param1, param2):
    """
    Brief description.
    
    Args:
        param1 (type): Description
        param2 (type): Description
    
    Returns:
        type: Description
    """
    pass
```

---

## 📚 Additional Resources

### Learning Resources

**PyQt6 Documentation:**
- Official Docs: https://www.riverbankcomputing.com/static/Docs/PyQt6/
- Tutorials: https://www.pythonguis.com/pyqt6-tutorial/

**VTK Documentation:**
- Official Docs: https://vtk.org/documentation/
- Examples: https://kitware.github.io/vtk-examples/site/Python/

**Medical Imaging:**
- NIfTI Format: https://nifti.nimh.nih.gov/
- SimpleITK: https://simpleitk.readthedocs.io/

**Segmentation Metrics:**
- Dice Coefficient: https://en.wikipedia.org/wiki/Sørensen–Dice_coefficient
- Hausdorff Distance: https://en.wikipedia.org/wiki/Hausdorff_distance

---

### Related Projects

- **3D Slicer**: Advanced medical imaging platform
- **ITK-SNAP**: Manual segmentation tool
- **MITK**: Medical imaging toolkit
- **TotalSegmentator**: AI segmentation model
- **nnU-Net**: State-of-the-art segmentation framework

---

## 📜 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📧 Contact & Support

### Get Help

- **GitHub Issues**: [Report bugs](https://github.com/yourusername/medical-segmentation-suite/issues)
- **Email**: your.email@example.com
- **Documentation**: [Wiki](https://github.com/yourusername/medical-segmentation-suite/wiki)

### Acknowledgments

**Special Thanks:**
- **VTK Development Team** - 3D visualization toolkit
- **SimpleITK Contributors** - Medical image processing
- **PyQt/Qt Team** - GUI framework
- **Medical Imaging Community** - Segmentation algorithms and datasets

**Citing This Work:**
```bibtex
@software{medical_segmentation_suite,
  title = {Medical Imaging Segmentation Suite},
  author = {Your Name},
  year = {2024},
  url = {https://github.com/yourusername/medical-segmentation-suite}
}
```

---

## ❓ FAQ (Frequently Asked Questions)

**Q: Can I use this for clinical diagnosis?**  
A: No, this is a research/educational tool. Not validated for clinical use.

**Q: What file formats are supported?**  
A: Currently only NIfTI (.nii.gz). DICOM support possible in future.

**Q: Can I add my own segmentation model?**  
A: Yes! Follow the "Adding New Organs" guide.

**Q: Why is loading slow?**  
A: Large NIfTI files (>256³) require processing. Files are auto-downsampled.

**Q: Can I export the 3D models?**  
A: Not currently, but see "Development Guide" for STL export code.

**Q: Does this work on Mac/Linux?**  
A: Yes, fully cross-platform (Windows, macOS, Linux).

**Q: How much RAM do I need?**  
A: Minimum 4GB, recommended 8GB+ for large datasets.

**Q: Can I change the color scheme?**  
A: Yes! Edit the `THEME` dictionary in `gui.py`.

**Q: Is GPU required?**  
A: No, but GPU acceleration improves performance for large models.

**Q: How do I report bugs?**  
A: Open an issue on GitHub with detailed description and error logs.

---

## 📊 Gallery

### Application Screenshots

**Organ Selection Screen:**
```
[Screenshot of main selection interface]
```

**Liver Analysis Workspace:**
```
[Screenshot showing 3D liver with controls]
```

**Kidney System Visualization:**
```
[Screenshot of kidney system with multiple parts]
```

**Model Comparison:**
```
[Side-by-side comparison screenshots]
```

---

## 🎓 Appendix

### Command Reference

**Installation & Setup:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run application
cd gui && python gui.py

# Check dependencies
python -c "import PyQt6, vtk, SimpleITK; print('OK')"

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Update dependencies
pip install --upgrade PyQt6 vtk SimpleITK numpy pandas
```

**Project Structure:**
```bash
# Create directories
mkdir -p Assets/{SwinUnter,Total-Segmentator,WholeBodyCt}/{Liver,Kidneys,Stomach}
mkdir -p Evaluation-Metrics
mkdir -p gui/icons

# List NIfTI files
find Assets -name "*.nii.gz"

# Check CSV files
cat Evaluation-Metrics/*.csv
```

---

### Version History

**v1.0.0** (December 2024)
- Initial release
- Support for 3 organs (Liver, Kidneys, Stomach)
- Support for 3 models (Swin UNETR, Total Segmentator, WholeBody CT)
- Interactive 3D visualization
- Real-time metric display
- Glassmorphic UI design

---

### System Requirements

**Minimum:**
- Python 3.8+
- 4GB RAM
- 500MB disk space
- OpenGL 2.1+
- 1280x720 display

**Recommended:**
- Python 3.10+
- 8GB RAM
- 2GB disk space
- OpenGL 3.3+
- 1920x1080 display
- Dedicated GPU

---

### Known Limitations

- NIfTI format only (no DICOM support yet)
- Single CT modality (no MRI support)
- Limited to 3 organ systems currently
- No real-time segmentation (pre-computed results only)
- No batch processing mode
- No export functionality (future feature)

---

### Roadmap

**Upcoming Features:**

- [ ] Export to STL/OBJ formats
- [ ] Screenshot capture
- [ ] Auto-rotation animation
- [ ] DICOM support
- [ ] Batch processing mode
- [ ] Additional organ systems
- [ ] MRI support
- [ ] Custom color schemes
- [ ] Multi-language support
- [ ] Cloud integration


---

**Last Updated**: December 2024  
**Version**: 1.0.0  
**Python**: 3.8+  
**Status**: ✅ Production Ready

---

**Built with ❤️ for the Medical Imaging Community**

*Making medical AI research accessible and visual*

---

**Star this project on GitHub!** ⭐

If you find this useful, please star the repository to show your support!
