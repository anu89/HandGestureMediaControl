Hand Gesture Recognition for Media Control 🎥🖐️
A Python-based application that uses real-time hand gesture recognition to control media playback (YouTube, VLC, etc.) using your webcam. No physical mouse or keyboard required—completely touchless!

🚀 Features
Hand Detection & Tracking: Leverages MediaPipe and OpenCV for fast, accurate hand landmark detection.

Gesture Recognition: Identifies key hand gestures and maps them to media actions:

Index Up → Next

Index+Middle Up → Back

Thumb+Index Up → Volume Up

Thumb Up → Volume Down

Fist → Play/Pause

Touchless Control: Triggers corresponding system/media hotkeys using pyautogui.

Visual Feedback: Shows detected gestures in real-time webcam feed for instant feedback.

Extensible: Easy to add custom gestures or actions.
📝 How to Use
Clone the Repository:

bash
git clone https://github.com/anu89/HandGestureMediaControl.git
cd HandGestureMediaControl
Install Requirements:

bash
pip install -r requirements.txt
Run the Application:

bash
python main.py
Get Started:

Allow webcam access when prompted.

Open YouTube (or any supported media player) and make sure the window is focused.

Use the following gestures:

Gesture	Action
Fist	Play/Pause
Index finger up	Next (Right)
Index+Middle up	Back (Left)
Thumb+Index up	Volume Up
Thumb only	Volume Down
Exit:

Press 'q' in the OpenCV window to quit.

📄 Requirements
Python 3.7+

Webcam

OS: Windows/Mac/Linux
