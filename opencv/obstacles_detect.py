import cv2
import numpy as np

def detect_obstacles(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    obstacles = []
    for contour in contours:
        # Filter contours based on area
        area = cv2.contourArea(contour)
        if area > 100:  # Adjust threshold as needed
            # Get bounding box of contour
            x, y, w, h = cv2.boundingRect(contour)
            obstacles.append((x, y, w, h))
            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame, obstacles

def determine_movement(obstacles, frame_width, frame_height):
    # Initialize directions
    move_left = move_right = move_forward = move_backward = False

    for obstacle in obstacles:
        x, y, w, h = obstacle
        # Determine obstacle position relative to the center of the frame
        obstacle_center_x = x + w / 2
        obstacle_center_y = y + h / 2
        center_x = frame_width / 2
        center_y = frame_height / 2

        if obstacle_center_x < center_x:
            move_left = True
        else:
            move_right = True

        if obstacle_center_y < center_y:
            move_forward = True
        else:
            move_backward = True

    return move_left, move_right, move_forward, move_backward

cap = cv2.VideoCapture(0)  # Change to video file if needed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect obstacles
    processed_frame, obstacles = detect_obstacles(frame)

    # Determine movement based on obstacles
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]
    move_left, move_right, move_forward, move_backward = determine_movement(obstacles, frame_width, frame_height)

    # Output movement commands
    if move_left:
        print("Move left")
    if move_right:
        print("Move right")
    if move_forward:
        print("Move forward")
    if move_backward:
        print("Move backward")

    cv2.imshow('Obstacle Detection', processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
