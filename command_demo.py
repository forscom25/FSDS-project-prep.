import time
import fsds

# connect to the AirSim simulator 
client = fsds.FSDSClient()

# Check network connection
client.confirmConnection()

# After enabling api controll only the api can controll the car. 
# Direct keyboard and joystick into the simulator are disabled.
# If you want to still be able to drive with the keyboard while also 
# controll the car using the api, call client.enableApiControl(False)
client.enableApiControl(True)

# Instruct the car to go full-speed forward
car_controls = fsds.CarControls()
car_controls.throttle = 1
client.setCarControls(car_controls)

time.sleep(5)

# Places the vehicle back at it's original position
client.reset()