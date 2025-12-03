# hand-approaches

# Hand Boundary Detection (SAFE / WARNING / DANGER)

This project is a real-time hand tracking and virtual boundary monitoring system built using **OpenCV**. It detects the user's hand using classical computer vision (no MediaPipe) and shows three states on the screen:

* **SAFE** – Hand is far away from the boundary
* **WARNING** – Hand is approaching the boundary
* **DANGER DANGER** – Hand touches or crosses the boundary

This project works fully offline and runs smoothly in **VS Code / local system**.

---

## 🚀 Features

✔ Real-time webcam feed (OpenCV)
✔ Hand detection using **skin color segmentation** (HSV mask)
✔ Virtual boundary line drawn on screen
✔ State logic using distance from boundary
✔ On-screen alerts (SAFE / WARNING / DANGER DANGER)
✔ CPU-only real-time performance (10–20 FPS)
✔ No MediaPipe, no OpenPose, no cloud API

---

## 📂 Project Structure

```
Hand_boundry/
│
├── handenv/                 # Virtual environment
│
└── hand_boundary_project.py # Main project file
```

---

## 🧰 Step 1 — Create Virtual Environment

Open terminal inside project folder and run:

```
python -m venv handenv
```

Then activate it:

### Windows

```
handenv\Scripts\activate
```

You should now see:

```
(handenv)
```

---

## 📦 Step 2 — Install Dependencies

Run:

```
pip install opencv-python numpy
```

---

## 🧾 Step 3 — Save the Code

Create file:

```
hand_boundary_project.py
```

Paste the full Python code provided in the project window.

---

## ▶️ Step 4 — Run the Project

Make sure environment is active:

```
(handenv)
```

Then run:

```
python hand_boundary_project.py
```

Your webcam will open and you will see:

* Boundary line
* Hand detection dot
* SAFE / WARNING / DANGER alerts

Press **Q** to quit.

---

## ⚙️ How It Works

1. Captures video frame from webcam
2. Converts frame to HSV
3. Applies skin color mask
4. Finds largest contour → assumed hand
5. Computes hand center position
6. Compares hand X-coordinate with boundary line
7. Shows state based on distance:

| Distance from Line | State   |
| ------------------ | ------- |
| < 25 px            | DANGER  |
| < 70 px            | WARNING |
| >= 70 px           | SAFE    |

---

## 🎯 Customization

### Change boundary position:

In code:

```
LINE_X = 300
```

Set any x-value (0–640).

### Improve skin detection:

Tune HSV range:

```
lower = [0, 30, 60]
upper = [20, 150, 255]
```

### Add sound alert:

I can add a beep or alarm in DANGER.

---

## 🛑 Common Issues & Fixes

### ❌ Webcam not opening

✔ Close any other app using camera (Zoom, Meet, Teams)
✔ Restart VS Code
✔ Try: `VideoCapture(1)` instead of 0

### ❌ Hand not detected

✔ Increase room lighting
✔ Move hand closer
✔ Adjust HSV range

---

## 📝 Future Enhancements

I can upgrade your project with:

* Fingertip detection
* Custom virtual shapes (box, circle)
* Gesture control
* Multi-hand detection
* Sound warnings

Just tell me what you want next!

---

## ✅ Author

Created with guidance fro
