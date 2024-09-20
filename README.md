# Electro-Monster-HandTracker
𝑨𝒏 𝒆𝒍𝒆𝒄𝒕𝒓𝒊𝒄 𝒎𝒐𝒏𝒔𝒕𝒆𝒓 𝒘𝒉𝒊𝒄𝒉 𝒇𝒐𝒍𝒍𝒐𝒘𝒔 𝒕𝒉𝒆 𝒎𝒐𝒗𝒆𝒎𝒆𝒏𝒕𝒔 𝒐𝒇 𝒚𝒐𝒖𝒓 𝒉𝒂𝒏𝒅 𝒐𝒏 𝒕𝒉𝒆 𝒔𝒄𝒓𝒆𝒆𝒏




# Electric Monster - Finger Tracker

This project uses Python, Pygame, OpenCV, and MediaPipe to create an **electric monster** that follows the movements of the user's index finger on the screen. The program captures video from the webcam, detects the position of the user's hand, and tracks the index finger tip to create a dynamic animation of tentacles following the finger’s movements.

## Features

- Real-time hand tracking using **MediaPipe**.
- An electric monster effect that dynamically reacts to your finger's movements.
- Smooth tentacle-like animations using **Pygame**.
- **Fullscreen** mode for an immersive experience.

## Demo

Watch the electric monster in action:


## Installation

Follow these steps to set up the project on your local machine:


### Prerequisites

- **Python 3.x**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Pygame**: Used for rendering and handling graphics.
- **OpenCV**: For accessing and processing webcam input.
- **MediaPipe**: For detecting and tracking the hand and finger movements.

### Install Required Dependencies

Use `pip` to install the necessary Python libraries:

```bash
pip install pygame opencv-python mediapipe
```

### Running the Project

1. **Clone this repository** to your local machine:

   ```bash
   git clone https://github.com/KianShojaei/Electro-Monster-HandTracker.git
   cd electric-monster-finger-tracker
   ```

2. **Run the script**:

   ```bash
   python main.py
   ```

The program will start, open a fullscreen window, and begin tracking your finger's movements. As you move your index finger in front of the camera, you’ll see a monster-like tentacle animation follow your finger.

## How It Works

1. **Hand Tracking**: The program uses **MediaPipe’s Hand solution** to track the user's hand position in real-time. It identifies the index finger tip coordinates and translates them into screen positions.
   
2. **Tentacle Animation**: Multiple tentacle-like segments are generated, which follow the finger’s movement. These segments adjust their position and angle to simulate the behavior of tentacles reaching out to the finger.

3. **Rendering**: **Pygame** is used for drawing the tentacles and rendering the animations on the screen in real-time.

## Controls

- Move your index finger in front of the webcam to control the monster's tentacles.
- Press `Esc` or `close` the window to exit the program.


## Future Enhancements

- Add more visual effects and colors to make the monster more vibrant and lifelike.
- Implement more complex behavior for tentacles, such as reacting to multiple fingers or hands.
- Optimize performance for smoother animations at higher frame rates.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Kian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
