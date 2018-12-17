#ds18b20 rpi, 1 wire, sudo pip3 install w1thermsensor
import w1thermsensor

sensor = w1thermsensor.W1ThermSensor()

temp = sensor.get_temperature()
print(temp)
