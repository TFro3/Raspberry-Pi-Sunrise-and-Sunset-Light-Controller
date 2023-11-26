import requests
from gpiozero import OutputDevice
from datetime import datetime, timedelta, timezone
import time

# Configuration variables
latitude = 'YOUR LATITUDE'
longitude = 'YOUR LONGITUDE'
relay_pin = 14  # Replace with your GPIO pin number

# Offset in minutes for sunrise and sunset
sunrise_time_offset = 0
sunset_time_offset = 0

# Function to get today's sunrise and sunset times from API
def get_today_sunrise_sunset(latitude, longitude):
    try:
        url = f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0'
        response = requests.get(url)
        data = response.json()

        sunrise = datetime.strptime(data['results']['sunrise'], "%Y-%m-%dT%H:%M:%S%z")
        sunset = datetime.strptime(data['results']['sunset'], "%Y-%m-%dT%H:%M:%S%z")

        print(f"Today's Sunrise: {sunrise.strftime('%Y-%m-%d %H:%M:%S %Z')}")
        print(f"Today's Sunset: {sunset.strftime('%Y-%m-%d %H:%M:%S %Z')}")

        return sunrise.replace(tzinfo=timezone.utc), sunset.replace(tzinfo=timezone.utc)
    except Exception as e:
        print(f"Error fetching sunrise/sunset times from API: {e}")
        return None, None

# Function to calculate time until the next sunset and sunrise
def time_until_next_sunrise_sunset(sunrise, sunset):
    now = datetime.now(timezone.utc)

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
relay = OutputDevice(relay_pin, active_high=False, initial_value=False)

# Fetch sunrise and sunset times for the day
today_sunrise, today_sunset = get_today_sunrise_sunset(latitude, longitude)

while True:
    now = datetime.now(timezone.utc)
    time_until_sunset, time_until_sunrise = time_until_next_sunrise_sunset(today_sunrise, today_sunset)

    # Determine the state of the relay based on sunset and sunrise times
    if time_until_sunset <= max(sunset_time_offset * 60, 0) and time_until_sunrise > 0:
        print("Sunset Hours Reached: LIGHTS ON")
        relay.on()
    else:
        print("Sunrise Hours Reached: LIGHTS OFF")
        relay.off()

    # Check if it's past midnight to fetch new sunrise and sunset times
    if now.hour == 0 and now.minute == 0:
        today_sunrise, today_sunset = get_today_sunrise_sunset(latitude, longitude)

    # Sleep for a while before checking again
    time.sleep(60)  # Sleep for 1 minute before rechecking
