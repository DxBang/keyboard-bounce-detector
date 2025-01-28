import time
from keyboard import on_press, wait

BOUNCE_THRESHOLD = 0.075

timer = None
last = None
ignore_key_codes = [
	42, # Left Shift
	54, # Right Shift
	56, # Alt
	29, # Left Ctrl
	93, # menu
	541, # alt gr
	72, # up arrow
	80, # down arrow
	75, # left arrow
	77, # right arrow
	82, # insert
	83, # delete
	71, # home
	79, # end
	73, # page up
	81, # page down
	69, # num lock & clear
	55, # print screen
	70, # scroll lock
	58, # caps lock
#	57, # space
	14, # backspace
	-173, # mute
	-174, # volume down
	-175, # volume up
	-176, # play next
	-177, # play previous
	-178, # stop
	-179, # play/pause
	91, # left windows
	92, # right windows
]

def bounce_detection(event):
	if event.scan_code in ignore_key_codes:
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
