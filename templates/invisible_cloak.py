"""
Real-time Invisibility Cloak using OpenCV
Press 'q' to quit, 's' to save current frame as image.
"""
import cv2
import numpy as np
import time

def get_background(cap, seconds=3):
    # Capture background frames for `seconds`, then compute median background
    print(f"Capturing background for {seconds} seconds. Please stay out of frame...")
    frames = []
    start = time.time()
    while time.time() - start < seconds:
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.flip(frame, 1)
        frames.append(frame)
        cv2.imshow('Capturing background (press Esc to skip)', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyWindow('Capturing background (press Esc to skip)')
    if not frames:
        raise RuntimeError("No frames captured for background.")
    # Use median to reduce noise / moving objects
    bg = np.median(frames, axis=0).astype(dtype=np.uint8)
    return bg

def make_invisible():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam. Check camera index or permissions.")
        return

    # Warm up camera
    for i in range(30):
        cap.read()

    background = get_background(cap, seconds=3)

    print("Now wear your cloak (preferably a solid color). Press 'q' to quit.")
    save_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)  # mirror view

        # Convert to HSV for color detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # ---------- Color range for cloak ----------
        # Default ranges detect RED (works well with red cloth). Red is tricky because it wraps HSV hue.
        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2

        # If your cloak is another color (green/blue), replace masks with appropriate ranges:
        # Example for green:
        # mask = cv2.inRange(hsv, np.array([35, 40, 40]), np.array([85, 255,255]))

        # Morphological operations to clean mask
        kernel = np.ones((3,3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
        mask = cv2.dilate(mask, kernel, iterations=1)

        # Inverse mask to get part without cloak
        mask_inv = cv2.bitwise_not(mask)

        # Use mask to extract non-cloak parts from the current frame
        res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)

        # Use mask to extract cloak area from background (so cloak pixels are replaced by background)
        res2 = cv2.bitwise_and(background, background, mask=mask)

        # Final output
        final = cv2.addWeighted(res1, 1, res2, 1, 0)

        # Show windows
        cv2.imshow('Original', frame)
        cv2.imshow('Mask', mask)
        cv2.imshow('Invisibility Cloak', final)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            fname = f'invisible_{save_count}.png'
            cv2.imwrite(fname, final)
            print(f"Saved {fname}")
            save_count += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    make_invisible()
