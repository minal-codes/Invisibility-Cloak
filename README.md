# 🪄 Invisibility Cloak using OpenCV

A Computer Vision project inspired by the Harry Potter invisibility cloak.

## Features

- Real-time webcam processing
- Detects red color cloth
- Replaces cloak area with captured background
- Uses OpenCV and NumPy

## Technologies Used

- Python
- OpenCV
- NumPy

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python invisibility_cloak.py
```

## How it Works

1. Captures the background.
2. Detects red color using HSV.
3. Removes noise using morphology.
4. Replaces the red region with the background.

## Author

Minal Sharma