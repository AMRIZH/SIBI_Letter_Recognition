import gradio as gr
import cv2
import onnxruntime as ort
import numpy as np

# Load the ONNX model
ort_session = ort.InferenceSession('runs/train/exp/weights/best.onnx')

def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

def recognize_image(frame):
    # Preprocess the frame
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (640, 640))  # Resize to the input size expected by the model
    img = img.transpose(2, 0, 1)  # Change data layout from HWC to CHW
    img = np.expand_dims(img, axis=0).astype(np.float32) / 255.0  # Normalize and add batch dimension

    # Run inference
    ort_inputs = {ort_session.get_inputs()[0].name: img}
    ort_outs = ort_session.run(None, ort_inputs)
    
    # Post-process the output (this part depends on your model's specific output format)
    # For simplicity, this example assumes you have a single output
    output = ort_outs[0]
    
    # Assuming the output needs to be converted back to an image
    # You may need to adjust this part according to your model's output format
    output = np.squeeze(output)
    output = np.transpose(output, (1, 2, 0))
    output = (output * 255).astype(np.uint8)
    
    return output

# Create a Gradio interface
gr.Interface(
    fn=recognize_image,
    inputs=gr.inputs.Image(source="webcam", tool="editor", streaming=True),
    outputs=gr.outputs.Image(type="auto"),
    live=True,
    title="Real-Time Image Recognition",
    description="Uses an ONNX model to perform real-time image recognition from a webcam."
).launch()
