# Keyboard Bounce Detector
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
```bash
Key 'space' pressed after 1.126027 seconds.
Key 'space' pressed after 0.791025 seconds.
Key 'space' pressed after 0.687029 seconds.
Key 'space' pressed after 0.890103 seconds.
Key 'space' pressed after 1.227010 seconds.
Key 'space' pressed after 0.948973 seconds.
Key 'space' pressed after 0.857048 seconds.
Key 'space' pressed after 0.935020 seconds.
Key 'space' pressed after 0.971063 seconds.
Key 'space' pressed after 0.910039 seconds.
Key 'space' pressed after 1.002995 seconds.
Key 'space' pressed after 0.941028 seconds.
Key 'space' pressed after 0.966068 seconds.
Key 'space' pressed after 1.026017 seconds.
Key 'space' pressed after 0.955106 seconds.
Key 'space' pressed after 0.985956 seconds.
Key 'space' pressed after 1.015056 seconds.
Bounce detected for key 'space' after 0.046905 seconds.
```
