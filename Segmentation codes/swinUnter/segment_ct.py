"""
CT Scan Segmentation using Swin UNETR (BTCV Model)
Segments 13 abdominal organs from CT scan
"""

import os
import torch
import nibabel as nib
import numpy as np
from scipy import ndimage
from monai.networks.nets import SwinUNETR
from monai.transforms import (
    Compose,
    LoadImage,
    EnsureChannelFirst,
    Orientation,
    Spacing,
    ScaleIntensityRange,
    EnsureType,
)
from monai.inferers import sliding_window_inference

# Organ labels for BTCV dataset
ORGAN_LABELS = {
    0: "Background",
    1: "Spleen",
    2: "Right Kidney",
    3: "Left Kidney",
    4: "Gallbladder",
    5: "Esophagus",
    6: "Liver",
    7: "Stomach",
    8: "Aorta",
    9: "Inferior Vena Cava (IVC)",
    10: "Portal and Splenic Veins",
    11: "Pancreas",
    12: "Right Adrenal Gland",
    13: "Left Adrenal Gland",
}


def load_model(model_path, device):
    """Load the Swin UNETR model with pretrained weights."""
    model = SwinUNETR(
        in_channels=1,
        out_channels=14,
        feature_size=48,
        depths=(2, 2, 2, 2),
        num_heads=(3, 6, 12, 24),
        use_checkpoint=False,
        spatial_dims=3,
    )
    
    # Load pretrained weights
    checkpoint = torch.load(model_path, map_location=device, weights_only=False)
    # Handle wrapped checkpoint format (state_dict key)
    if "state_dict" in checkpoint:
        state_dict = checkpoint["state_dict"]
    else:
        state_dict = checkpoint
    
    # Strip 'module.' prefix if present (from DataParallel training)
    new_state_dict = {}
    for k, v in state_dict.items():
        if k.startswith("module."):
            new_state_dict[k[7:]] = v  # Remove 'module.' prefix
        else:
            new_state_dict[k] = v
    
    model.load_state_dict(new_state_dict)
    model = model.to(device)
    model.eval()
    
    return model


def preprocess_ct(image_path):
    """Preprocess CT scan for inference."""
    transforms = Compose([
        LoadImage(image_only=True, reader="ITKReader"),
        EnsureChannelFirst(),
        Orientation(axcodes="RAS"),
        Spacing(pixdim=(1.5, 1.5, 2.0), mode="bilinear"),
        ScaleIntensityRange(a_min=-175, a_max=250, b_min=0.0, b_max=1.0, clip=True),
        EnsureType(),
    ])
    
    # Also load the original image for metadata
    loader = LoadImage(image_only=False, reader="ITKReader")
    original_data = loader(image_path)
    
    processed = transforms(image_path)
    return processed, original_data


def run_inference(model, image, device):
    """Run sliding window inference on the CT scan."""
    with torch.no_grad():
        image = image.unsqueeze(0).to(device)  # Add batch dimension
        
        # Sliding window inference
        outputs = sliding_window_inference(
            inputs=image,
            roi_size=(96, 96, 96),
            sw_batch_size=4,
            predictor=model,
            overlap=0.5,
        )
        
        # Apply softmax and get argmax for segmentation
        outputs = torch.softmax(outputs, dim=1)
        outputs = torch.argmax(outputs, dim=1)
        
    return outputs.squeeze(0).cpu().numpy()


def resample_to_original(segmentation, original_shape):
    """Resample segmentation back to original CT dimensions using nearest neighbor."""
    # Calculate zoom factors for each dimension
    zoom_factors = [
        original_shape[i] / segmentation.shape[i]
        for i in range(3)
    ]
    
    # Use nearest neighbor interpolation for labels (order=0)
    resampled = ndimage.zoom(segmentation, zoom_factors, order=0, mode='nearest')
    
    return resampled.astype(np.int16)


def save_segmentation(segmentation, reference_image, output_path):
    """Save segmentation as NIfTI file."""
    # Create NIfTI image with same affine as reference
    if hasattr(reference_image, 'affine'):
        affine = reference_image.affine
    else:
        # Default affine if not available
        affine = np.eye(4)
    
    seg_nifti = nib.Nifti1Image(segmentation.astype(np.int16), affine)
    nib.save(seg_nifti, output_path)
    print(f"Segmentation saved to: {output_path}")


def main():
    # Paths
    base_dir = r"C:\Users\Youssef\Desktop\huhu"
    model_path = os.path.join(base_dir, "swin_unetr_btcv_segmentation", "models", "model.pt")
    input_ct_path = os.path.join(base_dir, "ct (2).nii.gz")
    output_path = os.path.join(base_dir, "segmentation_output.nii.gz")
    
    # Check if GPU is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Load model
    print("Loading Swin UNETR model...")
    model = load_model(model_path, device)
    print("Model loaded successfully!")
    
    # Preprocess CT scan
    print(f"Loading and preprocessing CT scan: {input_ct_path}")
    processed_ct, original_data = preprocess_ct(input_ct_path)
    print(f"Preprocessed CT shape: {processed_ct.shape}")
    
    # Run inference
    print("Running segmentation (this may take a few minutes)...")
    segmentation = run_inference(model, processed_ct, device)
    print(f"Segmentation complete! Shape: {segmentation.shape}")
    
    # Print detected organs
    unique_labels = np.unique(segmentation)
    print("\nDetected organs:")
    for label in unique_labels:
        if label in ORGAN_LABELS:
            count = np.sum(segmentation == label)
            print(f"  {label}: {ORGAN_LABELS[label]} ({count} voxels)")
    
    # Load original NIfTI for shape and affine
    original_nifti = nib.load(input_ct_path)
    original_shape = original_nifti.shape
    
    # Resample segmentation to match original CT dimensions
    print(f"\nResampling segmentation from {segmentation.shape} to {original_shape}...")
    segmentation_resampled = resample_to_original(segmentation, original_shape)
    print(f"Resampled segmentation shape: {segmentation_resampled.shape}")
    
    # Verify labels are preserved after resampling
    unique_labels_resampled = np.unique(segmentation_resampled)
    print(f"Labels after resampling: {unique_labels_resampled}")
    
    # Save segmentation with original affine
    save_segmentation(segmentation_resampled, original_nifti, output_path)
    
    print("\n[SUCCESS] Segmentation complete!")
    print(f"Output saved to: {output_path}")
    print(f"Segmentation dimensions match original CT: {segmentation_resampled.shape}")
    print("The segmentation can now be directly overlayed on the original CT.")


if __name__ == "__main__":
    main()
