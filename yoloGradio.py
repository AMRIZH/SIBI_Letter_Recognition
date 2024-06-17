import gradio as gr
from ultralytics import YOLO

# Load the trained model (adjust the path to the correct model file)
model = YOLO("runs/train/exp/weights/best.pt")

# Define a function for inference
def predict(image):
    # Perform inference
    results = model(image)
    # Get the output image with bounding boxes and labels
    output_image = results.plot()
    return output_image

# Set up Gradio interface to use webcam
interface = gr.Interface(
    fn=predict,  # Function to call for prediction
    inputs=gr.inputs.Image(source="webcam", type="pil"),  # Input type: Webcam (PIL)
    outputs=gr.outputs.Image(type="pil"),  # Output type: Image (PIL)
    live=True  # Enable live mode
)

# Launch the interface
interface.launch()
