# main.py - reads the sensor and prints the values
# Needs hs3003.py uploaded to the board as well.
import time
from hs3003 import HS3003

sensor = HS3003()

while True:
    t, h = sensor.read()
    print("Temp: {:.1f} C  Humidity: {:.1f} %" .format(t, h))
    time.sleep(2)