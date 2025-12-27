import os
import nibabel as nib
import numpy as np
import pandas as pd
from monai.metrics import compute_dice, compute_hausdorff_distance, compute_iou
import torch

def load_nifti(path):
    img = nib.load(path)
    data = img.get_fdata()
    return data, img.affine

def calculate_metrics(y_pred, y):
    # Ensure they are binary masks (0 or 1)
    y_pred = (y_pred > 0.5).astype(np.float32)
    y = (y > 0.5).astype(np.float32)
    
    # Convert to torch tensors and add batch/channel dims [B, C, H, W, D]
    y_pred_tensor = torch.from_numpy(y_pred).unsqueeze(0).unsqueeze(0)
    y_tensor = torch.from_numpy(y).unsqueeze(0).unsqueeze(0)
    
    # Dice
    dice = compute_dice(y_pred_tensor, y_tensor, ignore_empty=False).item()
    
    # IoU
    iou = compute_iou(y_pred_tensor, y_tensor, ignore_empty=False).item()
    
    # Hausdorff Distance (HD95 is common but let's provide standard HD or as requested)
    # MONAI compute_hausdorff_distance returns standard HD if percentile is not specified
    try:
        if np.sum(y_pred) == 0 or np.sum(y) == 0:
            hd = np.nan
        else:
            hd = compute_hausdorff_distance(y_pred_tensor, y_tensor, percentile=95).item()
    except Exception as e:
        print(f"Error computing Hausdorff: {e}")
        hd = np.nan
        
    return dice, iou, hd

def evaluate_model(model_name, model_dir, gt_dir, prefix=""):
    results = []
    organs = ["Kidneys", "Liver", "Stomach"]
    
    for organ in organs:
        gt_organ_dir = os.path.join(gt_dir, organ)
        model_organ_dir = os.path.join(model_dir, organ)
        
        if not os.path.exists(gt_organ_dir) or not os.path.exists(model_organ_dir):
            print(f"Skipping {organ} for {model_name} as directory is missing")
            continue
            
        gt_files = [f for f in os.listdir(gt_organ_dir) if f.endswith('.nii.gz')]
        
        for gt_file in gt_files:
            model_file = f"{prefix}{gt_file}"
            gt_path = os.path.join(gt_organ_dir, gt_file)
            model_path = os.path.join(model_organ_dir, model_file)
            
            if not os.path.exists(model_path):
                print(f"Warning: Model file {model_file} not found for {model_name} in {organ}")
                continue
            
            print(f"Evaluating {model_name} - {organ} - {gt_file}...")
            y_gt, _ = load_nifti(gt_path)
            y_pred, _ = load_nifti(model_path)
            
            if y_gt.shape != y_pred.shape:
                print(f"Shape mismatch for {gt_file}: GT {y_gt.shape}, Pred {y_pred.shape}. Skipping.")
                continue
                
            dice, iou, hd = calculate_metrics(y_pred, y_gt)
            results.append({
                "Organ": organ,
                "File": gt_file,
                "Dice": dice,
                "IoU": iou,
                "Hausdorff95": hd
            })
            
    df = pd.DataFrame(results)
    output_file = f"{model_name}_metrics.csv"
    df.to_csv(output_file, index=False)
    print(f"Saved results for {model_name} to {output_file}")
    
    # Save a summary as well
    summary = df.groupby("Organ").mean(numeric_only=True).reset_index()
    summary_file = f"{model_name}_summary.csv"
    summary.to_csv(summary_file, index=False)
    print(f"Saved summary for {model_name} to {summary_file}")
    
    return output_file

if __name__ == "__main__":
    GT_DIR = r"C:\Users\Youssef\Desktop\Lulu\Assets\Ground-Truths"
    
    models = [
        {"name": "TotalSegmentator", "dir": r"C:\Users\Youssef\Desktop\Lulu\Assets\Total-Segmentator", "prefix": "ct_"},
        {"name": "SwinUnter", "dir": r"C:\Users\Youssef\Desktop\Lulu\Assets\SwinUnter", "prefix": ""},
        {"name": "WholeBodyCt", "dir": r"C:\Users\Youssef\Desktop\Lulu\Assets\WholeBodyCt", "prefix": ""}
    ]
    
    for model in models:
        evaluate_model(model["name"], model["dir"], GT_DIR, model["prefix"])
