from machine import Pin,freq
from time import sleep
import sys
from hx711 import HX711

# calibration with start program ctrl+c then hx.tara on different weights

if sys.platform == "esp8266":
    dpclk=Pin(16) # D0=16
    dout=Pin(5) #  D1=5
    taste=Pin(0,Pin.IN,Pin.PULL_UP) # D3=0
else:
    dpclk=Pin(3) # D2=3
    dout=Pin(2) #  D1=2
    taste=Pin(1,Pin.IN,Pin.PULL_UP) # D0=2

hx = HX711(dout,dpclk,1)
hx.wakeUp()
hx.tara(25)
hx.calFaktor(35)
    
while 1:
    if taste.value() == 0:
        hx.tara(10)
    m="{:0.2f}".format(hx.masse(10))
    print(m)
    sleep(0.5)
