import streamlit as st
import cv2
import numpy as np
import os
from datetime import datetime

# Load the pre-trained Haar Cascade model for face detection
face_cascade = cv2.CascadeClassifier('facedetection/haarcascade_frontalface_default.xml')

# Function to detect faces
def detect_faces(frame, scaleFactor, minNeighbors, color):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    return frame, faces

# Function to save image with detected faces
def save_image(frame, faces):
    if len(faces) > 0:
        # Create an output folder if not exists
        if not os.path.exists('detected_faces'):
            os.makedirs('detected_faces')
        
        # Save image with timestamp to avoid overwriting
        filename = os.path.join('detected_faces', f"face_detected_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
        cv2.imwrite(filename, frame)
        return filename
    return None

def main():
    # App title and description
    st.title("Face Detection with Streamlit")
    st.markdown("""
    This app uses your webcam to detect faces in real-time.
    You can customize the detection parameters, including:
    - Adjusting the **color** of the face rectangles
    - Modifying the **scaleFactor** and **minNeighbors** values for face detection
    - Saving images with detected faces to your device
    - Enabling a **mirror effect** on the webcam feed
    """)

    # Add instructions
    st.write("""
    - The app will automatically show the webcam feed.
    - You can adjust the parameters using the sliders below.
    - Click the button to save the image with detected faces.
    - The webcam feed will have a mirror effect.
    """)

    # Color picker for rectangle color
    rect_color = st.color_picker('Select Rectangle Color', '#0000FF')  # Default color: Blue
    # Convert hex to RGB (Streamlit uses RGB) and then convert to BGR for OpenCV
    rect_color_bgr = (
        int(rect_color[5:7], 16),  # Red
        int(rect_color[3:5], 16),  # Green
        int(rect_color[1:3], 16)   # Blue
    )

    # Sliders for scaleFactor and minNeighbors
    scale_factor = st.slider('Adjust scaleFactor', 1.05, 1.5, 1.1, 0.01)
    min_neighbors = st.slider('Adjust minNeighbors', 1, 10, 3)

    # Create a placeholder to display the webcam video feed
    placeholder = st.empty()

    # Access the webcam
    cap = cv2.VideoCapture(0)  # 0 is the default camera

    if not cap.isOpened():
        st.error("Could not access webcam.")
        return

    # Button to save the image
    save_button = st.button("Save Image with Detected Faces")

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame.")
            break

        # Apply the mirror effect (flip horizontally)
        frame = cv2.flip(frame, 1)

        # Detect faces in the frame
        frame_with_faces, faces = detect_faces(frame, scale_factor, min_neighbors, rect_color_bgr)

        # Convert the frame to RGB (OpenCV uses BGR by default)
        frame_rgb = cv2.cvtColor(frame_with_faces, cv2.COLOR_BGR2RGB)

        # Show the frame with face detection in Streamlit
        placeholder.image(frame_rgb, channels="RGB", use_column_width=True)

        # If the save button is pressed, save the image
        if save_button:
            saved_image = save_image(frame_with_faces, faces)
            if saved_image:
                st.success(f"Image saved as: {saved_image}")
            else:
                st.warning("No faces detected, so no image was saved.")

    # Release the webcam when done
    cap.release()

if __name__ == "__main__":
    main()
