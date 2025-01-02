import time
from keyboard import on_press, wait

BOUNCE_THRESHOLD = 0.075

last_keystroke_time = None
last_key = None

def bounce_detection(event):
	global last_keystroke_time, last_key
	current_time = time.perf_counter()
	if last_keystroke_time is not None:
		time_diff = current_time - last_keystroke_time
		if event.name == last_key and time_diff < BOUNCE_THRESHOLD:
			print(f"Bounce detected for key '{event.name}' after {time_diff:.6f} seconds.")
	last_keystroke_time = current_time
	last_key = event.name

on_press(bounce_detection)

print("Listening for keystrokes... Press ESC to exit.")
wait('esc')
