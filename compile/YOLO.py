import sys
import ctypes
import os
import cv2
import numpy as np
from mss import mss
from ultralytics import YOLO
from pathlib import Path

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("relaunching")
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    sys.exit()

if getattr(sys, 'frozen', False):
    script_dir = Path(sys.executable).resolve().parent
else:
    script_dir = Path(__file__).resolve().parent

model_path = script_dir / "best.pt"
print("Looking for model at:", model_path)

model = YOLO(str(model_path))
model.to('cpu')

dummy = np.zeros((340, 640, 3), dtype=np.uint8)
model(dummy)

screen_width, screen_height = 1920, 1080
capture_width, capture_height = 640, 340
center_x = screen_width // 2
center_y = screen_height // 2

monitor = {
    "top": center_y - capture_height // 2,
    "left": center_x - capture_width // 2,
    "width": capture_width,
    "height": capture_height
}

sct = mss()
cv2.namedWindow("YOLOv8 Screen Detection", cv2.WINDOW_NORMAL)

frame_count = 0
coord_path = script_dir / "coords.txt"

while True:
    frame_count += 1

    screen_img = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(screen_img, cv2.COLOR_BGRA2BGR)

    results = model(frame, verbose=False)
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = f"{model.names[cls]} {conf:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            target_x = monitor["left"] + (x1 + x2) // 2 - 100
            target_y = monitor["top"] + (y1 + y2) // 2 + 50

            with open(coord_path, "w") as f:
                f.write(f"{target_x} {target_y}")

            break

    cv2.imshow("YOLOv8 Screen Detection", frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
