import RPi.GPIO as GPIO
import time
from datetime import datetime
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--runtime', type= float, required= True)
parser.add_argument('--filename', type = str, required = True )
args = parser.parse_args()
runtime = args.runtime
filename = args.filename
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

radiation_sensor_pin = 27  # Replace this with the GPIO pin number you connected the SIG to
GPIO.setup(radiation_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 0

def count_callback(channel):
    global count
    count += 1

GPIO.add_event_detect(radiation_sensor_pin, GPIO.FALLING, callback=count_callback, bouncetime=10)
reft = time.time() + runtime
curr = 0
times = []
counts = []
while(curr <= reft):
    time.sleep(60)
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - Counts detected: {count}")
    times.append(timestamp)
    counts.append(count)
    count = 0
    curr = time.time()
    


dict = {'time':times, 'counts': counts}
df = pd.DataFrame(dict)
df.to_csv(filename)
