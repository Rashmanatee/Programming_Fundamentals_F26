# main.py - reads the sensor and prints the values based on user input
# Needs hs3003.py uploaded to the board as well
import time
from hs3003 import HS3003 

sensor = HS3003()

valid_options = ["T", "H", "0"]

def read_and_display_temp(sensor_device):
    
    t = sensor_device.temperature()
    
    reading_id = random.randint(1, 100)
    
    print("Reading #{}: Temp: {:.1f} C".format(reading_id, t))

def read_and_display_hum(sensor_device):
    
    h = sensor_device.humidity()
    
    reading_id = random.randint(1, 100)
    print("Reading #{}: Humidity: {:.1f} %".format(reading_id, h))
    
while True:
    
    print("\nPlease choose from the following options:")
    print("T - Temperature")
    print("H - Humidity")
    print("0 - Both")
    
    
    user_choice = input("Enter your choice: ")
    
    
    user_choice = user_choice.upper()

    if user_choice == "T":
        read_and_display_temp(sensor)
    else:
        if user_choice == "H":
            read_and_display_hum(sensor)
        else:
            if user_choice == "0":
                read_and_display_temp(sensor)
                read_and_display_hum(sensor)
            else:
                
                print("Invalid choice. Please try again.")

