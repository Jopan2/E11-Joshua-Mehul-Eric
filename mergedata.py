import adafruit_bme680
import time
import argparse
import board
import pandas as pd
import numpy as np
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
import serial
from adafruit_pm25.uart import PM25_UART

reset_pin = None

uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.95)

pm25 = PM25_UART(uart, reset_pin)

i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25
t = []
T = []
g = []
h = []
p = []
a = []
pm10 = []
pm2 = []
pm100 = []
parser = argparse.ArgumentParser()
parser.add_argument('--runtime', type= float, required= True)
parser.add_argument('--filename', type = str, required = True )
args = parser.parse_args()
a = time.time() + args.runtime
filename = args.filename
while time.time()<a:
    t.append(time.ctime())
    T.append(bme680.temperature)
    g.append(bme680.gas)
    h.append(bme680.relative_humidity)
    p.append(bme680.pressure)
    a.append(bme680.altitude)
    aqdata = pm25.read()
    pm10.append(aqdata["pm10 standard"])
    pm2.append(aqdata["pm25 standard"])
    pm100.append(aqdata["pm100 standard"])

    time.sleep(1)

dict = {'time':t, 'temp':T, 'gas':g, 'humidity':h, 'pressure':p, 'altitude':a, "PM 1.0": aqdata["pm10 standard"],  "PM 2.5":aqdata["pm25 standard"] ,"PM10":aqdata["pm100 standard"]}
df = pd.DataFrame(dict)
df.to_csv(filename)

