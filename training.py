import os
import shutil
import time
from ultralytics import YOLO
from roboflow import Roboflow

# Download dataset from Roboflow
api_key = "WM2DGQ6I2MwnMn0ViPz5"  # Replace with your Roboflow API key
workspace = "amzah"
project_name = "sibi_letterlevel_dataset-gniwb"
version_number = 2

print("Downloading dataset from Roboflow...")
rf = Roboflow(api_key=api_key)
project = rf.workspace(workspace).project(project_name)
version = project.version(version_number)
dataset = version.download("folder")  # Path to downloaded dataset

# Rename 'valid' to 'val' for YOLO compatibility
os.rename('./sibi_letterlevel_dataset-2/valid', './sibi_letterlevel_dataset-2/val')          # MUNGKIN PERLU DIUBAH

# Train with YOLO v11 using a configurable model
model_choice = "yolo11m-cls"  # Choose from "yolo11n-cls", "yolo11s-cls", "yolo11m-cls", "yolo11l-cls"
epochs = 200
img_size = 640
patience = 5
dataset_path = "./sibi_letterlevel_dataset-2"          # MUNGKIN PERLU DIUBAH

print("Training YOLO model...")
os.system(
    f"yolo task=classify mode=train model={model_choice}.pt data={dataset_path} epochs={epochs} imgsz={img_size} patience={patience}"
)

# Define the path to the trained model
model_path = "./runs/classify/train/weights/best.pt"           # MUNGKIN PERLU DIUBAH

# Export the trained model to various formats
export_formats = ["saved_model", "tflite", "coreml", "onnx", "openvino"]

print("Exporting the trained model to various formats...")
for fmt in export_formats:
    os.system(f"yolo export model={model_path} format={fmt}")

# Zip and download the entire trained folder
output_zip = "trained_e200_p5_claasify.zip"
trained_folder = "./runs"          # MUNGKIN PERLU DIUBAH
print("Zipping the trained folder...")
shutil.make_archive("trained_e200_p5_claasify", 'zip', trained_folder)

print(f"Training complete. The zipped trained folder is saved as {output_zip}.")
