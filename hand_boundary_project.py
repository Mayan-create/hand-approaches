import cv2
import numpy as np

LINE_X = 300   # virtual boundary line (x-axis)

def get_hand_position(frame):
    """Detect hand using skin color mask and return center point."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Skin color range (tunable)
    lower = np.array([0, 30, 60], dtype=np.uint8)
    upper = np.array([20, 150, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.GaussianBlur(mask, (7, 7), 0)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return None

    c = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(c)

    cx = x + w // 2
    cy = y + h // 2

    return (cx, cy)


def classify_state(x):
    dist = abs(x - LINE_X)

    if dist < 25:
        return "DANGER"
    elif dist < 70:
        return "WARNING"
    else:
        return "SAFE"


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    hand_pos = get_hand_position(frame)

    # Draw virtual line
    cv2.line(frame, (LINE_X, 0), (LINE_X, frame.shape[0]), (255, 0, 0), 2)

    state = "SAFE"

    if hand_pos is not None:
        x, y = hand_pos
        cv2.circle(frame, (x, y), 8, (0, 255, 0), -1)

        state = classify_state(x)

        if state == "DANGER":
            cv2.putText(frame, "DANGER DANGER", (70, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 4)
        elif state == "WARNING":
            cv2.putText(frame, "WARNING", (150, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 255, 255), 4)
        else:
            cv2.putText(frame, "SAFE", (190, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 255, 0), 4)

    cv2.imshow("Hand Boundary System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
