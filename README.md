<h1 align="center"> Invisibility Cloak</h1>

<h3 align="center">
Real-Time Computer Vision System
</h3>

<p align="center">
A real-time Computer Vision application that creates an invisibility effect using
<strong>OpenCV</strong>, <strong>MediaPipe</strong>, and <strong>Python</strong> by replacing the segmented foreground with a dynamically captured background.
</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-FF6F00?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Completed-32CD32?style=for-the-badge"/>

</p>

---

##  Overview

Ghost / Invisibility Mode is an interactive real-time computer vision project that recreates the famous **invisibility cloak illusion**.

The application captures a clean background during calibration and continuously segments the user from the live camera feed. When the invisibility mode is activated using hand gestures, the segmented foreground is seamlessly replaced with the stored background, creating the illusion that the user has disappeared.

The project combines **background modeling**, **human segmentation**, **hand tracking**, and **gesture recognition** to deliver a smooth and engaging real-time experience.

---

#  Features

-  Real-time webcam processing
-  Live invisibility effect
-  Hand gesture based activation
-  Dynamic portal generation
-  Automatic background calibration
-  Screenshot capture
-  Background recalibration
-  Optimized real-time performance
-  Cross-platform support

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| OpenCV | Image Processing & Video Stream |
| MediaPipe | Selfie Segmentation & Hand Tracking |
| NumPy | Numerical Computation |

---

# Working

The application follows the following pipeline:

```
Camera Input
      │
      ▼
Background Calibration
      │
      ▼
Selfie Segmentation
      │
      ▼
Hand Tracking
      │
      ▼
Gesture Detection
      │
      ▼
Background Replacement
      │
      ▼
Real-Time Invisibility Effect
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/Invisibility-Computer-Vision.git
```

Move into the project folder

```bash
cd Invisibility-Computer-Vision
```

Install dependencies

```bash
pip install opencv-python numpy mediapipe
```

---

# Running the Project

Default webcam

```bash
python main.py
```

Specify a camera

```bash
python main.py 1
```

---

# Controls

| Key | Function |
|------|----------|
| **R** | Recalibrate Background |
| **S** | Save Screenshot |
| **Q** | Quit |
| **ESC** | Exit Application |

---

# ✋ Gesture Guide

### Step 1

Stand still for **3 seconds** while the application captures the background.

### Step 2

Show **both hands** and spread them apart.

A yellow portal box will appear between your hands.

### Step 3

Pinch your **thumb** and **index finger** together.

The invisibility mode will activate.

### Step 4

Repeat the pinch gesture to become visible again.

---

# 📂 Project Structure

```
Invisibility-Computer-Vision
│
├── engine.py
├── main.py
├── requirements.txt
├── README.md
```

---

# 📸 Demo

> Add your screenshots or GIF here.

```
screenshots/demo.gif
```

---

# 🔮 Future Improvements

- Multiple invisibility modes
- AI-based gesture customization
- GPU acceleration
- Performance optimization
- Custom visual effects
- Video recording support

---

# 👨‍💻 Developer

**Minal Sharma**

AI & Machine Learning Enthusiast

Passionate about building practical Computer Vision and AI applications.

---

## ⭐ If you found this project helpful, consider giving it a star!
