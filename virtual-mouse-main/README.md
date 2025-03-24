# Virtual Mouse by Dheeraj 🖱️

This project uses MediaPipe and OpenCV to create a virtual mouse controlled by hand gestures. With the power of computer vision, your webcam becomes a smart interface to move the cursor, click, and even scroll! 🚀

## Features 🌟
- **Cursor Movement**: Move the mouse pointer using your index finger.
- **Left Click**: Tap your thumb and index finger together to perform a left click.
- **Scrolling**: Use raised index and middle fingers for scrolling up and down.

## Requirements 📦
- Python 3.7+
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

Install dependencies using pip:
```bash
pip install opencv-python mediapipe pyautogui numpy
```

## How It Works 🖐️
1. **Hand Detection**: MediaPipe detects hand landmarks through your webcam.
2. **Gesture Recognition**: Index and thumb positions are analyzed for click and cursor movements.
3. **Mouse Control**: PyAutoGUI translates gestures into system-level mouse actions.

## Usage 💻
1. Clone the repository:
   ```bash
   git clone https://github.com/DheerajNair123/virtual-mouse.git
   cd virtual-mouse
   ```
2. Run the script:
   ```bash
   python app.py
   ```
3. Allow access to your webcam when prompted.
4. Control your mouse using hand gestures! 🖐️✨

## Controls 🎮
- **Cursor Movement**: Move your index finger to control the pointer.
- **Left Click**: Pinch index and thumb together.
- **Scroll**: Raise both index and middle fingers; move index above or below middle for scrolling.

## Exit 🚪
Press `q` to quit the application.

## Tutorial for cloning
- **Yotube Link:** [https://youtu.be/0614YOZs3Ow]

## License 📜
This project is open-source and available under the MIT License. Feel free to modify and enhance it! 🌈

---

**Created by Dheeraj** 💡

Enjoy the magic of hand gestures and elevate your interaction with computers! 🖥️✨

