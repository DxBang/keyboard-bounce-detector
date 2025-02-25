"""
Keybounce detection script.
By: Daniel Bang, Bang Systems
"""

import time
import keyboard
import csv
import json
from typing import Dict, List

BOUNCE_THRESHOLD: float = 0.05  # inhumanly fast
BOUNCE_CSVFILE: str = "results.csv"
BOUNCE_JSONFILE: str = "results.json"
IGNORE_KEYS: List[int] = [
	-173,  # mute
	-174,  # volume down
	-175,  # volume up
	-176,  # play next
	-177,  # play previous
	-178,  # stop
	-179,  # play/pause
]
results: Dict[int, Dict[str, any]] = {}
bounced: Dict[str, List[float]] = {}

# read the contents of the .version file
__version__ = "0.0.0"
with open(".version") as f:
	__version__ = f.read().strip()


def bounce_detection(event: keyboard.KeyboardEvent) -> None:
	"""Detect key bounce events."""
	if event.scan_code in IGNORE_KEYS:
		return
	now = time.perf_counter()
	state = event.event_type == 'down'
	#print(f"({event.scan_code}) = '{event.name}' {event.event_type}")
	if event.scan_code not in results:
		results[event.scan_code] = {
			'name': event.name,
			'time': now,
			'state': state,
			'pressed': 1,
			'bounced': 0
		}
		return
	key_event = results[event.scan_code]
	if key_event['state'] == state:
		# key is held down
		key_event['time'] = now
		return
	# check for bounce
	diff = now - key_event['time']
	if state == True and diff < BOUNCE_THRESHOLD:
		print(f"Bounce {diff:.6f}s on '{event.name}' ({event.event_type})")
		key_event['bounced'] += 1
		if event.name not in bounced:
			bounced[event.name] = []
		bounced[event.name].append(diff)
	if state == True:
		key_event['pressed'] += 1
	key_event['state'] = state
	key_event['time'] = now

def save_results() -> None:
	"""Save results to CSV and JSON files."""
	with open(BOUNCE_CSVFILE, 'w', newline='', encoding='utf-8') as f:
		csvwriter = csv.writer(f, delimiter=',', lineterminator='\n')
		csvwriter.writerow(['scan_code', 'name', 'pressed', 'bounced'])
		for scan_code, key_event in results.items():
			csvwriter.writerow([scan_code, key_event['name'], key_event['pressed'], key_event['bounced']])
	print(f" Saved CSV: {BOUNCE_CSVFILE}")
	with open(BOUNCE_JSONFILE, 'w', encoding='utf-8') as f:
		json.dump({
			'version': __version__,
			'bounce': bounced,
			'result': {k: {kk: vv for kk, vv in v.items() if kk not in ['time', 'state']} for k, v in results.items()},
		}, f, indent="\t")
	print(f"Saved JSON: {BOUNCE_JSONFILE}")

def main() -> None:
	"""Main function to start key bounce detection."""
	keyboard.hook(bounce_detection)
	print(f"Keybounce detection script v{__version__}")
	print("Start hitting those keys like a maniac.")
	print("\nPress Ctrl+F10 to save & exit.")
	keyboard.wait("ctrl+f10")
	save_results()

if __name__ == "__main__":
	main()
