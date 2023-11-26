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

Using a map or website such as https://www.latlong.net/ input your city to get your relative coordinates. Locate the section of code below in the program and edit it with your own coordinates.
```python3
# Configuration variables
latitude = 'YOUR LATITUDE'
longitude = 'YOUR LONGITUDE'
```
