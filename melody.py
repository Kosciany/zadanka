import pigpio
import time

tempo = 1
cala = tempo
pol = tempo/2
cwierc = tempo/4
osemka = tempo/8

C = 261
D = 294
E = 330
F = 350
G = 392
A = 440
H = 494
C_2 = 523


class PiTone:
  buzzer = 24 #pin 12 pinem silnika
  def __init__(self):
    self.pi = pigpio.pi()
  def spiewaj(nuty,czas):
    if len(nuty) is not len(czasy):
      return -1
    for i in range (0,len(nuty)):
      self.pi.set_PWM_dutycycle(buzzer,nuty[i])
      time.sleep(czasy[i]-0.1)
      self.pi.set_PWM_dutycycle(buzzer,0)
      time.sleep(0.1)
    self.pi.set_PWM_dutycycle(buzzer,0)
    
    
    
sto_lat_nuty =[G,E,G,E,G,A,G,F,E,F
               F,D,F,D,F,G,F,E,D,E
               G,G,E,G,G,E,G,C,H,A,G,A
               H,H,H,C]
sto_lat_czas =[pol, pol, pol, pol, pol, cwierc, cwierc, cwierc, cwierc, pol,
               pol, pol, pol, pol, pol, cwierc, cwierc, cwierc, cwierc, pol
               cwierc,cwierc, pol, cwierc, cwierc, pol, pol, cwierc, cwierc, cwierc, cwierc, pol,
               cala, pol, pol, cala]
               
grajek = PiTone()
grajek.spiewaj(sto_lat_nuty, sto_lat_czas)
        
