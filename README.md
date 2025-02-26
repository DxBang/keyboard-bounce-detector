# Keyboard Chattering/Bounce Detection
_Detects keyboard chattering/bounce by monitoring the time between key presses._  
_by Bang Systems_  

## Introduction
Run the script in the background and press the space key multiple times. The script will detect if there is a keyboard bounce within a given time frame of 0.075 seconds. The time frame can be adjusted in the script.  
_Note: The script will not work against key holding._  

## Installation
### Linux
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Output
```text
Bounce detected for key 'space' after 0.046905 seconds.
Bounce detected for key 'm' after 0.046960 seconds.
Bounce detected for key 'r' after 0.043264 seconds.
Bounce detected for key 'n' after 0.058708 seconds.
Bounce detected for key 'v' after 0.043977 seconds.
```
