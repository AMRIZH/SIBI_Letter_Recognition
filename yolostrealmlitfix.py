import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np

# Load the trained model (adjust the path to the correct model file)
model = YOLO("C:/Amri/MY_LAB/yolo/repo/runs/classify/train/weights/best.pt")

# Title of the web app
st.title("Real-time Sign Language Recognition")

# Select webcam
webcam_index = st.selectbox('Select Webcam', [0, 1], index=0)

# Webcam input
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
st.subheader("Inference Result:")

cap = cv2.VideoCapture(webcam_index)

while run:
    ret, frame = cap.read()
    if not ret:
        st.error(
            "Failed to capture image from webcam. Please check the selected webcam index.")
        break

    # Convert the frame to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform inference
    results = model(frame)

    # Display all detection results
    inference_output = []
    if results and results[0].boxes is not None:
        for box in results[0].boxes.xyxy:
            label = model.names[int(box[5])]
            confidence = float(box[4])
            inference_output.append(f"{label} {confidence:.2f}")

    # Display the inference results in the format you specified
    if inference_output:
        st.write(f"Inference Results: {', '.join(inference_output)}")
    else:
        st.write("No signs detected.")

    # Display the output image
    FRAME_WINDOW.image(frame)

cap.release()
