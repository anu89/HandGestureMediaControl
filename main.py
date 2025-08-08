import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Helper function to detect which fingers are up
def fingers_up(hand_landmarks):
    finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    fingers = []
    # Thumb
    if hand_landmarks.landmark[finger_tips[0]].x < hand_landmarks.landmark[finger_tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)
    # Other fingers
    for tip in finger_tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip-2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

# Capture video from webcam
cap = cv2.VideoCapture(0)
with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    prev_gesture = None
    gesture_time = time.time()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip and convert the image
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Draw hand landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Get finger status
                fingers = fingers_up(hand_landmarks)

                # Gesture definitions
                gesture = None
                if fingers == [0,1,0,0,0]:  # Index finger up: Next
                    gesture = "Next"
                elif fingers == [0,1,1,0,0]:  # Index+middle: Back
                    gesture = "Back"
                elif fingers == [1,1,0,0,0]:  # Thumb+index pinch: Volume Up
                    gesture = "VolumeUp"
                elif fingers == [1,0,0,0,0]:  # Thumb only: Volume Down
                    gesture = "VolumeDown"
                elif fingers == [0,0,0,0,0]:  # Fist: Play/Pause
                    gesture = "PlayPause"

                # Cooldown/avoid repeated triggers
                if gesture and (gesture != prev_gesture or time.time()-gesture_time>1):
                    if gesture == "Next":
                        pyautogui.press('right')
                    elif gesture == "Back":
                        pyautogui.press('left')
                    elif gesture == "VolumeUp":
                        pyautogui.press('volumeup')
                    elif gesture == "VolumeDown":
                        pyautogui.press('volumedown')
                    elif gesture == "PlayPause":
                        pyautogui.press('space')
                    prev_gesture = gesture
                    gesture_time = time.time()

                # Display gesture on screen
                if gesture:
                    cv2.putText(frame, f"Gesture: {gesture}", (50,50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.imshow('Gesture Control', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
