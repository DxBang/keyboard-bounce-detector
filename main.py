"""
Keybounce detection script.
By: Daniel Bang, Bang Systems
"""
import time
import keyboard
import csv
import json
import argparse
from typing import Dict, List

# Constants
BOUNCE_THRESHOLD: float = 0.035  # inhumanly fast
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

# Global variables
results: Dict[int, Dict[str, any]] = {}
bounced: Dict[int, Dict[str, any]] = {}

# read the contents of the .version file
__version__: str = "0.0.0"
with open(".version") as f:
	__version__ = f.read().strip()

def load_results() -> None:
	"""Load results json file."""
	global results, bounced
	try:
		with open(BOUNCE_JSONFILE, 'r', encoding='utf-8') as f:
			data = json.load(f)
			results = {int(k): v for k, v in data.get('result', {}).items()}
			bounced = {int(k): v for k, v in data.get('bounce', {}).items()}
		print(f"Loaded results from: {BOUNCE_JSONFILE}")
	except FileNotFoundError:
		print(f"No previous results found. Starting fresh.")
		results = {}
		bounced = {}
	except Exception as e:
		print(f"Error: {e}")

def save_results() -> None:
	"""Save results to CSV and JSON files."""
	try:
		print(f"Saving CSV: {BOUNCE_CSVFILE}", end=" ")
		with open(BOUNCE_CSVFILE, 'w', newline='', encoding='utf-8') as f:
			csvwriter = csv.writer(f, delimiter=',', lineterminator='\n')
			csvwriter.writerow(['code', 'name', 'pressed', 'bounced'])
			for scan_code, key_event in results.items():
				csvwriter.writerow([scan_code, key_event['name'], key_event['pressed'], key_event['bounced']])
			print("[✓]")
	except Exception as e:
		print(f"[✗] {e}")
	try:
		print(f"Saving JSON: {BOUNCE_JSONFILE}", end=" ")
		with open(BOUNCE_JSONFILE, 'w', encoding='utf-8') as f:
			json.dump({
				'version': __version__,
				'bounce': bounced,
				'result': {k: {**v, 'state': False, 'time': 0} for k, v in results.items()}
			}, f, indent="\t")
			print("[✓]")
	except Exception as e:
		print(f"[✗] {e}")

def bounce_detection(event: keyboard.KeyboardEvent) -> None:
	"""Detect key bounce events."""
	try:
		if event.scan_code in IGNORE_KEYS:
			return
		now = time.perf_counter()
		state = event.event_type == 'down'
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
			print(f"Bounce {diff:.6f}s on '{event.name}'")
			key_event['bounced'] += 1
			if event.scan_code not in bounced:
				bounced[event.scan_code] = {
					'name': event.name,
					'time': []
				}
			bounced[event.scan_code]['time'].append(diff)
		if state == True:
			key_event['pressed'] += 1
		key_event['state'] = state
		key_event['time'] = now
	except Exception as e:
		print(f"Error: {e}")

def main() -> None:
	"""Main function to start key bounce detection."""
	parser = argparse.ArgumentParser()
	parser.add_argument('--reset', action='store_true', help='Reset results')
	args = parser.parse_args()

	if args.reset:
		results = {}
		bounced = {}
		print("Results reset.")
	else:
		load_results()

	keyboard.hook(bounce_detection)
	print(f"Keybounce detection script v{__version__}")
	print("Start hitting those keys like a maniac,\n or let it run in the background for a normal day.")
	print()
	print("Press Ctrl+F10 to save & exit.")
	keyboard.wait("ctrl+f10")
	save_results()

if __name__ == "__main__":
	main()
