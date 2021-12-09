from machine import Pin
from time import sleep

led = Pin(23, Pin.OUT)
led.off()

'''
Turn on/off LED every 250ms
'''
while True:
  led.value(not led.value())
  sleep(0.25)