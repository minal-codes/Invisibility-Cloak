import cv2
import numpy as np
import time
import os

# -------------------------------
# Open Webcam
# -------------------------------
camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Camera warm-up
time.sleep(2)

print("===================================")
print("Move out of the camera view.")
print("Capturing background in 5 seconds...")
print("===================================")

time.sleep(5)

# Capture Background
ret, background = camera.read()

if not ret:
    print("Failed to capture background!")
    camera.release()
    exit()

background = cv2.flip(background, 1)

print("Background Captured Successfully!")

# Create Window
cv2.namedWindow("Invisibility Cloak", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Invisibility Cloak", 640, 480)

# Kernel for noise removal
kernel = np.ones((3, 3), np.uint8)

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# Video Recording Variables
recording = False
video_writer = None

while True:

    ret, frame = camera.read()

    if not ret:
        break

    # Mirror Image
    frame = cv2.flip(frame, 1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red Color Range 1
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    # Red Color Range 2
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Create Masks
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    # Remove Noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)

    mask_inv = cv2.bitwise_not(mask)

    # Background Part
    background_part = cv2.bitwise_and(background, background, mask=mask)

    # Current Frame Part
    current_part = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Final Output
    final_output = cv2.add(background_part, current_part)

    # Instructions
    cv2.putText(
        final_output,
        "B = New Background | S = Screenshot | R = Record | ESC = Exit"
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    if recording:
        cv2.putText(
            final_output,
            "REC",
            (560, 30),
             cv2.FONT_HERSHEY_SIMPLEX,
             0.8,
             (0, 0, 255),
             2
        )

    if recording:
        video_writer.write(final_output)

    # Show Output
    cv2.imshow("Invisibility Cloak", final_output)

    key = cv2.waitKey(1) & 0xFF

    # ESC -> Exit
    if key == 27:
        break

    # B -> Capture New Background
    elif key == ord('b'):

        print("Move out of the frame...")
        time.sleep(3)

        ret, background = camera.read()

        if ret:
            background = cv2.flip(background, 1)
            print("New Background Captured!")

    # S -> Save Screenshot
    elif key == ord('s'):

        filename = os.path.join(
            "output",
            f"output_{int(time.time())}.png"
        )

        cv2.imwrite(filename, final_output)
        print(f"Screenshot Saved: {filename}")

    elif key == ord('r'):
        
        if not recording:

         filename = os.path.join(
            "output",
            f"recording_{int(time.time())}.mp4"
        )

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        video_writer = cv2.VideoWriter(
            filename,
            fourcc,
            20,
            (640, 480)
        )

        recording = True
        print("Recording Started")

    else:

        recording = False

        if video_writer is not None:
            video_writer.release()

        print("Recording Saved")

if video_writer is not None:
    video_writer.release()

camera.release()
cv2.destroyAllWindows()