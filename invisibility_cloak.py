import cv2
import numpy as np
import time

# Open webcam
camera = cv2.VideoCapture(0)

# Camera warm-up
time.sleep(2)

print("Please move out of the camera view.")
print("Capturing background in 5 seconds...")
time.sleep(5)

ret, background = camera.read()

if not ret:
    print("Failed to capture background.")
    camera.release()
    exit()

# Mirror the background
background = cv2.flip(background, 1)

print("Background captured!")

while True:
    ret, frame = camera.read()

    if not ret:
        break

    # Mirror frame
    frame = cv2.flip(frame, 1)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color ranges
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    # Remove noise
    kernel = np.ones((3, 3), np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)

    mask_inv = cv2.bitwise_not(mask)

    # Background where red cloth exists
    background_part = cv2.bitwise_and(background, background, mask=mask)

    # Current frame without red cloth
    current_part = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine both
    final_output = cv2.addWeighted(background_part, 1, current_part, 1, 0)

    cv2.imshow("Invisibility Cloak", final_output)

    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()