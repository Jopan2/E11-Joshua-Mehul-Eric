import adafruit_bme680
import time
import board
import pandas as pd
import numpy as np

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25
x = time.time()
y=0
t = []
T = []
g = []
h = []
p = []
a = []

arr = np.array(["Time","Temperature: %0.1f C","Gas: %d ohm","Humidity: %0.1f %%","Pressure: %0.3f hPa","Altitude = %0.2f meters"])
while y-x <= 5:
    print("\n " + time.ctime(), end = ", ")
    print("Temperature: %0.1f C" % bme680.temperature,end = ", ")
    print("Gas: %d ohm" % bme680.gas, end = ", ")
    print("Humidity: %0.1f %%" % bme680.relative_humidity, end = ", ")
    print("Pressure: %0.3f hPa" % bme680.pressure, end = ", ")
    print("Altitude = %0.2f meters" % bme680.altitude)
    t.append(time.ctime())
    T.append(bme680.temperature)
    g.append(bme680.gas)
    h.append(bme680.relative_humidity)
    p.append(bme680.pressure)
    a.append(bme680.altitude)
                            
    y = time.time()
    

    time.sleep(2)
dict = {'time':t, 'temp':T, 'gas':g, 'humidity':h, 'pressure':p, 'altitude':a}
    
DF = pd.DataFrame(dict)

DF.to_csv("data2.csv")