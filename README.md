# Raspberry-Pi-Sunrise-and-Sunset-Light-Controller
A simple controller to turn on and off a relay based on the sunrise and sunset times based on your location.

Features: 
- Automated Control: Automatically turns on a connected device (via relay) at sunset and off at sunrise.
- Customizable Offsets: Offers offsets for fine-tuning the activation and deactivation times relative to sunset and sunrise.
- Fetches Data from API: Retrieves accurate sunset and sunrise times using latitude and longitude coordinates.

Requirements: 
- Raspberry Pi
- Python 3
- 'gpiozero' library (for controlling GPIO pins)
- Internet connectivity to fetch sunset/sunrise times via an API


```python3
# Configuration variables
latitude = 'YOUR LATITUDE'
longitude = 'YOUR LONGITUDE'
```
