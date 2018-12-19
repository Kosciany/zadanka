import pigpio
from time import sleep

pi = pigpio.pi()     

led1 = 10
led2 = 9
led3 = 11
led4 = 22
read_pin = 5

while True:
  while True:
      if pi.read(read_pin) is 1:
          break
  pi.write(led1, 1) 
  pi.write(led2, 1) 
  sleep(1)
  pi.write(led3, 1)
  pi.write(led4, 1)
  sleep(1)
  pi.write(led1,0)
  pi.write(led2,0)
  pi.write(led3,0)
  pi.write(led4,0)
  sleep(1)
