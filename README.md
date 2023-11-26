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
Example: 
- Nashville, TN has the latitude & longitude values of 36.162663 and -86.781601 so that would be setup as shown below.
```python3
# Configuration variables
latitude = '36.162663'
longitude = '-86.781601'
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



> [!CAUTION]
> **Disclaimer:**
> 
> -  This project involves working with electrical circuits and high voltage components. Incorrect wiring or handling of high voltage lines can pose serious risks of electric shock or fire hazards. It's crucial to follow proper safety precautions and guidelines when working with high voltage.
> 
> **Safety Recommendations**
>
> - Qualified Personnel: It's strongly advised to involve or consult with qualified personnel or electricians when dealing with high voltage lines.
> 
> - Disconnect Power: Always disconnect power sources before working on electrical circuits.
> 
> - Insulation: Ensure proper insulation of wires and components to prevent accidental contact with live circuits.
> 
> - Proper Wiring: Follow manufacturer instructions and local electrical codes when wiring high voltage lines.
> 
> - Use Enclosures: Enclose circuits in suitable cases to prevent accidental contact.
> 
> - Safety Gear: Wear appropriate safety gear, such as gloves and goggles, when handling electrical components.
> 
>
> **Liability Statement**
>
> - The creators or contributors of this project do not accept any liability or responsibility for any damages, accidents, injuries, or losses resulting from the use, misuse, or inability to use the information or instructions provided in this project. Users assume all risks associated with handling high voltage circuits and should exercise caution and expertise when working on such systems.


Have fun and enjoy!
