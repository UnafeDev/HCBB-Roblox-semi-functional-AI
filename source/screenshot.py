import os
import time
import keyboard
import pyautogui

save_dir = "screenshots"
os.makedirs(save_dir, exist_ok=True)

print("Press '/' to start")
print("Press 'q' to stop")

recording = False

while True:
    if keyboard.is_pressed('/') and not recording:
        print("Started screenshot capture...")
        recording = True
        count = 1
    elif keyboard.is_pressed('q'):
        print("Stopped screenshot capture.")
        break

    if recording:
        screenshot = pyautogui.screenshot()
        filename = f"screenshot_{count}.png"
        filepath = os.path.join(save_dir, filename)
        screenshot.save(filepath)
        print(f"Saved {filename}")
        count += 1