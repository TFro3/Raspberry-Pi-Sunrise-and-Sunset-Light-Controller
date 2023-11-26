# Raspberry-Pi-Sunrise-and-Sunset-Light-Controller
A simple controller to turn on and off a relay based on the sunrise and sunset times based on your location.

Features: 
- Automated Control: Automatically turns on a connected device (via relay) at sunset and off at sunrise.
- Customizable Offsets: Offers offsets for fine-tuning the activation and deactivation times relative to sunset and sunrise.
- Fetches Data from API: Retrieves accurate sunset and sunrise times using latitude and longitude coordinates.

Requirements: 
- Raspberry Pi
- 5v Relay
- Python 3
- 'gpiozero' library (for controlling GPIO pins)
- Internet connectivity to fetch sunset/sunrise times via an API

To install:
- Run ```https://github.com/TFro3/Raspberry-Pi-Sunrise-and-Sunset-Light-Controller.git``` OR copy the code and create a new python file and paste it in.
- ```pip install gpiozero requests``` if you don't have gpiozero or requests already
- Then run the program using ```python3 LightController.py``` OR ```python3 'YourFileName'.py```

Using a map or website such as https://www.latlong.net/ input your city to get your relative coordinates. Locate the section of code below in the program and edit it with your own coordinates.
```python3
# Configuration variables
latitude = 'YOUR LATITUDE'
longitude = 'YOUR LONGITUDE'
```
You can also create an offset time to trigger the relays before, at, or after the sunrise/sunset time. 

```python3
# Offset in minutes for sunrise and sunset. Negative minutes allowed to trigger relays before set time.
sunrise_time_offset = 0
sunset_time_offset = 0
```
Examples:
- -10 (triggers relay 10 minutes before the sunrise/sunset time)
- 0 (triggers relay at the sunrise/sunset time)
- 10 (triggers relay 10 minutes after the sunrise/sunset time)

Have fun and enjoy!
