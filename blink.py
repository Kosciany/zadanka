import pigpio
from time import sleep

pi = pigpio.pi()     

led1 = 10
led2 = 11
led3 = 13
led4 = 14

while True:
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
