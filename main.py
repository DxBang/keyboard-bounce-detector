import time
from keyboard import on_press, wait

BOUNCE_THRESHOLD = 0.075

timer = None
last = None
ignore_keys = [
	-173, # mute
	-174, # volume down
	-175, # volume up
	-176, # play next
	-177, # play previous
	-178, # stop
	-179, # play/pause
	14, # backspace
	29, # Left Ctrl
	42, # Left Shift
	54, # Right Shift
	55, # print screen
	56, # Alt
	58, # caps lock
	69, # num lock & clear
	70, # scroll lock
	71, # home
	72, # up arrow
	73, # page up
	75, # left arrow
	77, # right arrow
	79, # end
	80, # down arrow
	81, # page down
	82, # insert
	83, # delete
	91, # left windows
	92, # right windows
	93, # menu
#	57, # space
	541, # alt gr
]

def bounce_detection(event):
	if event.scan_code in ignore_keys:
		return
	global timer, last
	now = time.perf_counter()
	if timer is not None:
		diff = now - timer
		if event.name == last.name and diff < BOUNCE_THRESHOLD:
			print(f"Bounce {diff:.6f}s on ({event.scan_code}) = '{event.name}'")
	timer = now
	last = event

on_press(bounce_detection)

print("Listening for keystrokes...\nPress F10 to exit.")
wait("f10")
