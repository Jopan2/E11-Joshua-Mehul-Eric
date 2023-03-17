import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

radiation_sensor_pin = 27  # Replace this with the GPIO pin number you connected the SIG to
GPIO.setup(radiation_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 0

def count_callback(channel):
    global count
    count += 1

GPIO.add_event_detect(radiation_sensor_pin, GPIO.FALLING, callback=count_callback, bouncetime=10)

try:
    while True:
        time.sleep(60)
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - Counts detected: {count}")
        count = 0

except KeyboardInterrupt:
    print("Script terminated.")
    GPIO.cleanup()
