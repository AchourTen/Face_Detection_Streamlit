# Face_Detection_Streamlit

A Streamlit-based web application that performs real-time face detection using OpenCV and the Haar Cascade classifier. The app provides an interactive interface for users to customize detection parameters and save images with detected faces.

## Features

- Real-time face detection using webcam feed
- Customizable detection parameters:
  - Rectangle color selection for face boundary boxes
  - Adjustable scale factor for detection sensitivity
  - Configurable minimum neighbors parameter
- Mirror effect on webcam feed for better user experience
- Ability to save snapshots with detected faces
- Intuitive user interface with live parameter adjustment


## Installation

1. Clone this repository:
```bash
git clone https://github.com/AchourTen/Face_Detection_Streamlit
cd Face_Detection_Streamlit

```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Dependencies

- Python 3.7+
- Streamlit
- OpenCV (cv2)
- NumPy

Create a `requirements.txt` file with the following:
```
streamlit
opencv-python
numpy
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. The app will open in your default web browser, and you'll see:
   - Live webcam feed with face detection
   - Color picker for rectangle customization
   - Sliders for adjusting detection parameters
   - Button to save images with detected faces

3. Adjust the parameters:
   - Use the color picker to change the face detection rectangle color
   - Adjust the `scaleFactor` 
   - Change the `minNeighbors`
   
         `scaleFactor`
      - Controls how much the image is resized in each scanning pass
      - Lower value (1.05): More accurate but slower
      - Higher value (1.3): Faster but might miss faces
      - Default: 1.1
        
         `minNeighbors`
      - Sets number of nearby detections needed to declare a face
      - Lower value (1-2): More detections, more false positives
      - Higher value (4-6): Fewer false positives, might miss faces
      - Default: 3

4. Click the "Save Image with Detected Faces" button to save the current frame with detected faces

## Project Structure

```
face-detection-app/
├── app.pyapp
├── facedetection/
│   └── haarcascade_frontalface_default.xml
├── requirements.txt
└── README.md
```

## Technical Details

### Face Detection Parameters

- `scaleFactor`: Determines how much the image size is reduced at each image scale (default: 1.1)
  - Smaller values = more accurate but slower
  - Larger values = faster but might miss faces
- `minNeighbors`: Specifies how many neighbors each candidate rectangle should have (default: 3)
  - Higher values = fewer false positives
  - Lower values = more detections but more false positives

### Output Directory

Detected faces are saved in the `detected_faces` directory with timestamps in the filename format: `face_detected_YYYYMMDD_HHMMSS.jpg`

## Troubleshooting

1. If the webcam doesn't start:
   - Ensure your webcam is properly connected
   - Check if other applications are using the webcam
   - Try running the app with administrator privileges

2. If face detection is not working well:
   - Adjust the `scaleFactor` and `minNeighbors` parameters
   - Ensure proper lighting conditions
   - Make sure faces are clearly visible in the camera

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Acknowledgments

- OpenCV for the Haar Cascade classifier
- Streamlit for the web interface framework
- The open-source community for various resources and inspiration
