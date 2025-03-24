
import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Screen resolution
screen_width, screen_height = pyautogui.size()

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get the landmarks
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the positions of the index finger (landmark 8) and middle finger (landmark 12)
            index_finger = hand_landmarks.landmark[8]
            middle_finger = hand_landmarks.landmark[12]
            thumb = hand_landmarks.landmark[4]

            # Convert the landmark positions to pixel coordinates
            index_x = int(index_finger.x * screen_width)
            index_y = int(index_finger.y * screen_height)
            thumb_x = int(thumb.x * screen_width)
            thumb_y = int(thumb.y * screen_height)

            # Check if index and middle fingers are raised
            if (hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and  # Index finger is raised
                hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y):  # Middle finger is raised
                # Enable scrolling
                pyautogui.scroll(-10 if index_finger.y > middle_finger.y else 10)

            elif hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y:  # Only index finger is raised
                # Move the cursor to the position of the index finger
                pyautogui.moveTo(index_x, index_y)

                # Calculate the distance between thumb and index finger for left click
                distance = np.sqrt((index_finger.x - thumb.x) ** 2 + (index_finger.y - thumb.y) ** 2)

                # Left-click if the distance is small (default behavior)
                if distance < 0.05:  # Arbitrary threshold for a click
                    pyautogui.click()

    # Show the frame
    cv2.imshow("Virtual Mouse By Dheeraj", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
