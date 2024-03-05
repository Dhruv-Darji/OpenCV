# Tarjani

Tarjani is a Python project designed to control the volume of your PC using hand gestures. It utilizes OpenCV for hand detection and tracking, as well as the pycaw library for controlling system volume.

## Project Overview

Tarjani detects the thumb and index finger of a hand using computer vision techniques. It calculates the distance between these two fingers and adjusts the volume of the PC accordingly.

## How it Works

The program captures video from the webcam, detects hands using the `MediaPipe` library, and identifies the thumb and index finger landmarks. It then calculates the distance between these landmarks and maps it to the system volume range.

MediaPipe is an open-source framework developed by Google that provides solutions for building multimodal applied machine learning pipelines. It offers various pre-built models and tools for processing and analyzing multimedia data, including images, videos, and audio.

## Dependencies

- **OpenCV (cv2):** Computer vision library for image and video processing.
- **MediaPipe (mediapipe):** Framework for building machine learning pipelines.
- **ctypes:** Foreign function library for calling functions in dynamic link libraries.
- **comtypes:** Python package for interacting with Component Object Model (COM) data types and interfaces.
- **pycaw:** Python library for interacting with the Windows Core Audio API.


You can install these dependencies using pip:

```bash
pip install opencv-python
```

```bash
pip install opencv-python mediapipe comtypes pycaw
```

## Usage

To use Tarjani:

1. Make sure your PC has a webcam connected and accessible.
2. Run the `tarjani.py` script.
3. Position your hand in front of the webcam with the thumb and index finger visible.
4. Adjust the distance between the thumb and index finger to control the volume.
5. Press 'q' to quit the program.

## Code Details

Here's a breakdown of the key components of the `tarjani.py` script:

- **Volume Control:** Utilizes the pycaw library to control the system volume based on the calculated distance between the thumb and index finger.
- **Hand Detection:** Uses the MediaPipe library to detect and track hand landmarks.
- **Landmark Calculation:** Extracts the coordinates of the thumb and index finger landmarks and calculates the distance between them.
- **Visualization:** Draws circles at the detected thumb and index finger positions, as well as a line between them for visualization purposes.

## Demo Video

<video width="640" height="360" controls>
  <source src="https://github.com/Dhruv-Darji/OpenCV/raw/dhruv/Tarjani%20Demo%20Video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

[Download Tarjani Demo Video](https://github.com/Dhruv-Darji/OpenCV/raw/dhruv/Tarjani%20Demo%20Video.mp4)


## Contributions

Contributions and feedback are welcome! Feel free to submit issues or pull requests to improve Tarjani. Also new ideas and processes are please to share.
