# Rescue Vision

This repository contains models and code for a camera-based AI system designed to detect road accidents and identify potential injuries, specifically blood presence and unconsciousness, in real-time. The system uses dashcam footage and in-cabin camera feeds to process frames, detect collisions, assess passenger conditions, and trigger alerts during critical events. The project is designed to support emergency response through real-time detection and analysis.

---

## Project Overview

Our AI-based system uses computer vision models to detect accidents and analyze injury presence in real-time. It consists of three main models:

1. **Accident Detection Model**: Detects accidents from dashcam footage using YOLO (You Only Look Once).  
2. **Blood Detection Model**: A CNN-based model that analyzes video frames to detect blood, distinguishing it from other red objects.  
3. **Unconsciousness Detection Model**: Uses head and eye position analysis to identify signs of unconsciousness in passengers.  

Both models work together to provide immediate alerts and evidence in case of an accident. Data is stored securely in the cloud, with automatic deletion every 30 days to optimize storage.

---

## Features

- **Real-Time Accident Detection**: Uses YOLO to detect collisions from dashcam video streams.  
- **Blood Detection**: Analyzes video frames to detect signs of injury in the cabin, distinguishing blood from other red objects.  
- **Unconsciousness Detection**: Monitors head tilt and eye closure patterns to assess passenger states.  
- **Automatic Alerts**: Sends alerts to emergency services and trusted contacts with the location, severity, and timestamps of the accident.  
- **Cloud Storage**: Stores video data securely for incident analysis, with automatic deletion after 30 days to optimize storage.  

---

## How It Works

1. **Accident Detection**  
   - The accident detection model processes dashcam footage to identify potential collisions.  
   - When an impact is detected, the system triggers further injury analysis and emergency alerting.  

2. **Blood Detection**  
   - Once an accident is identified, the blood detection model activates, analyzing video frames to check for visible blood.  
   - The CNN-based model distinguishes blood from other red-colored objects by analyzing texture, saturation, and shading, minimizing false positives.  

3. **Unconsciousness Detection**  
   - The unconsciousness detection model assesses head tilt and eye closure patterns in passengers.  
   - This helps identify individuals who may be unconscious or severely injured, prioritizing emergency response.  

---

## Technical Details

- **Accident Detection**: Trained using YOLO (You Only Look Once) to detect collision events from front-facing camera feeds.  
- **Blood Detection**: The CNN model processes video frames from in-cabin cameras to detect blood.  
- **Unconsciousness Detection**: Utilizes computer vision techniques to evaluate head and eye positions for unconsciousness indicators.  
- **Frame-by-Frame Analysis**: All models process video frames individually, ensuring high accuracy and reducing false alerts.  

---

## Prerequisites

- Python 3.10  
- TensorFlow (for CNN model)  
- OpenCV  
- YOLOv5 (for accident detection)  

---

## Visual Examples

1. **Presence of Blood in Accident**  
   ![Presence of blood in accident](https://github.com/user-attachments/assets/05222ab7-22a9-4304-b582-9488bb9a9e96)  

2. **Blood Correctly Identified**  
   ![Blood correctly identified](https://github.com/user-attachments/assets/ed4b5d43-03b2-4769-b689-8a5204ba5280)  

3. **Red Object (Not Blood)**  
   ![Red object](https://github.com/user-attachments/assets/3c68bdea-6494-4c3f-83dc-a897d837639f)  

4. **Object Not Confused with Blood**  
   ![Object not confused with blood](https://github.com/user-attachments/assets/11edcebd-81be-4453-9efb-aed94eeba487)  

---

## Future Scope

- Integration with IoT sensors for enhanced accident severity analysis.  
- Expansion to include more injury indicators, such as posture analysis and vital signs monitoring.  
- Real-time vehicle-to-vehicle (V2V) communication for collaborative road safety improvements.  

