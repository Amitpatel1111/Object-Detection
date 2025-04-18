import os
import cv2
import time
import uuid

# Path to store collected images
IMAGE_PATH = "CollectedImages"
labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']
number_of_images = 5

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)

    # Open camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Error: Cannot open camera")
        continue

    print(f"📷 Collecting images for '{label}' in 3 seconds...")
    time.sleep(3)

    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to capture image")
            continue

        imagename = os.path.join(img_path, f"{label}.{str(uuid.uuid1())}.jpg")
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)

        # Wait for 2 seconds or until 'q' is pressed
        if cv2.waitKey(2000) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
