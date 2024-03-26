import cv2
import numpy as np

# Function to calculate area in square centimeters
def calculate_area(contour, pixels_per_metric):
    area = cv2.contourArea(contour)
    return area / (pixels_per_metric ** 2)

# Function to find largest contour
def find_largest_contour(contours):
    if len(contours) == 0:
        return None
    return max(contours, key=cv2.contourArea)

# Start capturing video from webcam
cap = cv2.VideoCapture(0)

# Initialize background subtractor
background_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fg_mask = background_subtractor.apply(frame)

    # Find contours
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find largest contour
    largest_contour = find_largest_contour(contours)

    if largest_contour is not None:
        # Get bounding rectangle
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Calculate area in square centimeters (assuming each pixel is 1 square centimeter)
        area_cm2 = calculate_area(largest_contour, 1)

        # Draw bounding box and display area
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'Area: {area_cm2:.2f} cm^2', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display frame
    cv2.imshow('Object Detection', frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
