# rpi-cam/check_for_human.py
import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Use the YOLOv8 nano model for better performance on Raspberry Pi

# =============================================================================
def check_for_human_draw_box(image_path, output_path):
    '''Check if there is any person in the image and draw bounding boxes'''
    # Load image
    img = cv2.imread(image_path)
    original_height, original_width = img.shape[:2]

    # Resize image to 640x640 for YOLOv8
    img_resized = cv2.resize(img, (640, 640))

    # Perform inference
    results = model(img_resized)

    # Parse results and draw bounding boxes
    person_detected = False
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            confidence = float(box.conf)  # Convert tensor to float
            if confidence > 0.5:  # Only consider detections with confidence > 0.5
                # Get bounding box coordinates and scale them back to the original image size
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                x1 = int(x1 * original_width / 640)
                y1 = int(y1 * original_height / 640)
                x2 = int(x2 * original_width / 640)
                y2 = int(y2 * original_height / 640)

                label = f"{model.names[class_id]}: {confidence:.2f}"
                color = (0, 255, 0) if class_id == 0 else (0, 0, 255)  # Green for person, red for others
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)  # Draw bounding box
                cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # Put label
                if class_id == 0:
                    person_detected = True

    # Save the image with bounding boxes
    cv2.imwrite(output_path, img)
    print(f"Output saved to {output_path}")

    if person_detected:
        print("Person detected")
    else:
        print("No person detected")

    return person_detected

# =============================================================================
def check_for_human(image_path):
    '''Check if there is any person in the image'''
    # Load image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (640, 640))  # Resize image to 640x640 for YOLOv8

    # Perform inference
    results = model(img)

    # Parse results
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            confidence = float(box.conf)  # Convert tensor to float
            if class_id == 0 and confidence > 0.5:  # Class ID 0 corresponds to 'person' in COCO dataset
                print(f"Person detected with confidence {confidence:.2f}")
                return True

    print("No person detected")
    return False

# Example usage
image_path = "/home/malithjkd/Documents/jkd-tools/rpi-cam/data/2024-11-22-08-44-02.jpg"

# get location from image_part from to create output_path
image_part_root = image_path.split("/")[-1] 
image_part = image_part_root.split(".")[0]
output_path = f"/home/malithjkd/Documents/jkd-tools/rpi-cam/data/{image_part}_output.jpg"

is_person_present = check_for_human(image_path)
#is_person_present = check_for_human_draw_box(image_path, output_path)
print(f"Is person present: {is_person_present}")
# =============================================================================