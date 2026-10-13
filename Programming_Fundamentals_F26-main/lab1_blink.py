import machine
import time
led = machine.Pin(13, machine.Pin.OUT)
print ("Starting blink program...")

while True:
    led.value(1)
    
    time.sleep(1)
    
    led.value(0)
    
    time.sleep(1)