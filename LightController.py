import requests
from gpiozero import OutputDevice
from datetime import datetime, timedelta
import time

# Configuration variables
latitude = 'YOUR_LATITUDE'
longitude = 'YOUR_LONGITUDE'
relay_pin = 14  # Replace with your GPIO pin number

# Fallback sunrise and sunset times (in 12-hour clock format with AM/PM)
fallback_sunrise_time = (7, 0, 'AM')  # 7:00 AM
fallback_sunset_time = (7, 0, 'PM')   # 7:00 PM

# Offset in minutes for sunrise and sunset
sunrise_time_offset = 0
sunset_time_offset = 0

# Function to convert 12-hour time to 24-hour time
def convert_to_24_hour(hour, minute, is_pm):
    if is_pm:
        return (hour + 12) % 24, minute
    return hour, minute

# Function to get today's sunrise and sunset times from API or fallback to default times
def get_today_sunrise_sunset(latitude, longitude):
    try:
        url = f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0'
        response = requests.get(url)
        data = response.json()

        sunrise = datetime.strptime(data['results']['sunrise'], "%Y-%m-%dT%H:%M:%S%z")
        sunset = datetime.strptime(data['results']['sunset'], "%Y-%m-%dT%H:%M:%S%z")

        print(f"Today's Sunrise: {sunrise.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Today's Sunset: {sunset.strftime('%Y-%m-%d %H:%M:%S')}")

        return sunrise, sunset
    except Exception as e:
        print(f"Error fetching sunrise/sunset times from API: {e}")
        # Use default fallback times if API call fails
        today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)

        # Convert 12-hour format to 24-hour format for fallback times
        default_sunrise_hour, default_sunrise_minute, is_pm_sunrise = fallback_sunrise_time
        default_sunset_hour, default_sunset_minute, is_pm_sunset = fallback_sunset_time

        default_sunrise = today.replace(*convert_to_24_hour(default_sunrise_hour % 12, default_sunrise_minute, is_pm_sunrise == 'PM'))
        default_sunset = today.replace(*convert_to_24_hour(default_sunset_hour % 12, default_sunset_minute, is_pm_sunset == 'PM'))

        print(f"Using Fallback Sunrise: {default_sunrise.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Using Fallback Sunset: {default_sunset.strftime('%Y-%m-%d %H:%M:%S')}")

        return default_sunrise, default_sunset

# Function to calculate time until the next sunset and sunrise
def time_until_next_sunrise_sunset(sunrise, sunset):
    now = datetime.utcnow()

    next_sunrise = sunrise.replace(year=now.year, month=now.month, day=now.day)
    next_sunset = sunset.replace(year=now.year, month=now.month, day=now.day)

    if now > next_sunset:
        next_sunset += timedelta(days=1)
    if now > next_sunrise:
        next_sunrise += timedelta(days=1)

    time_until_sunset = (next_sunset - now).total_seconds()
    time_until_sunrise = (next_sunrise - now).total_seconds()

    return time_until_sunset, time_until_sunrise

# GPIO Pin for the relay
relay = OutputDevice(relay_pin)

while True:
    # Get today's sunrise and sunset times (fallback to defaults if API call fails)
    today_sunrise, today_sunset = get_today_sunrise_sunset(latitude, longitude)

    time_until_sunset, time_until_sunrise = time_until_next_sunrise_sunset(today_sunrise, today_sunset)

    if time_until_sunset < time_until_sunrise:
        time.sleep(time_until_sunset + sunset_time_offset * 60)
        print("Relay ON")
        relay.on()
        time_until_sunset, time_until_sunrise = time_until_next_sunrise_sunset(today_sunrise, today_sunset)
        time.sleep(time_until_sunset)
        print("Relay OFF")
        relay.off()
    else:
        time.sleep(time_until_sunrise + sunrise_time_offset * 60)
        print("Relay OFF")
        relay.off()
        time_until_sunset, time_until_sunrise = time_until_next_sunrise_sunset(today_sunrise, today_sunset)
        time.sleep(time_until_sunrise)
        print("Relay ON")
        relay.on()
