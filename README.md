# Rescue Vision

This repository contains models and code for a camera-based AI system designed to detect road accidents and identify potential injuries, specifically blood presence, in real-time. The system uses dashcam footage and in-cabin camera feeds to process frames, detect collisions, and trigger alerts when critical events occur. The project is designed to support emergency response through real-time detection and analysis.

## Project Overview

Our AI-based system uses computer vision models to detect accidents and analyze injury presence in real-time. It consists of two main models:

1. **Accident Detection Model**: Detects accidents from dashcam footage using YOLO (You Only Look Once).
   ![Accident detection model in motion](images and videos/accident ai main.mp4)

2. **Blood Detection Model**: A CNN-based model that analyzes video frames to detect blood, distinguishing it from other red objects.

Both models work together to provide immediate alerts and evidence in case of an accident. Data is stored securely in the cloud, with automatic deletion every 30 days to optimize storage.

---

### Features

- **Real-Time Accident Detection**: Uses YOLO to detect collisions from dashcam video streams.
- **Blood Detection**: Analyzes video frames to detect signs of injury in the cabin, distinguishing blood from other red objects.
- **Automatic Alerts**: Sends alerts to emergency services and trusted contacts with the location, severity, and timestamps of the accident.
- **Cloud Storage**: Stores video data securely for incident analysis, with automatic deletion after 30 days to optimize storage.

---

### How It Works

1. **Accident Detection**: 
   - The accident detection model processes dashcam footage to identify potential collisions.
   - When an impact is detected, the system triggers further injury analysis and emergency alerting.

2. **Blood Detection**: 
   - Once an accident is identified, the blood detection model activates, analyzing video frames to check for visible blood.
   - Our CNN-based model is trained to distinguish blood from other red-colored objects by analyzing texture, saturation, and shading, minimizing false positives.

---

### Technical Details

- **Accident Detection**: The model is trained using YOLO (You Only Look Once) to detect collision events from front-facing camera feeds.
- **Blood Detection**: The CNN model processes video frames from in-cabin cameras to detect blood.
- **Frame-by-Frame Analysis**: The blood detection model processes each video frame individually to confirm the presence of blood, helping reduce false alerts.

#### Prerequisites
- Python 3.10
- TensorFlow (for CNN model)
- OpenCV
- YOLOv5 (for accident detection)

