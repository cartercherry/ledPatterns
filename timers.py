######################################################################
# timers.py shows led patterns on 5 leds synchronized to music       #
# data stored in myData.py and imported for each led                 #
# hardware timer used to synchronize leds with music                 #
# stock royalty free music from https://stock.adobe.com/             #
######################################################################

from machine import Pin, Timer  #timer used to synchronize with music
import myData # state (ON/OFF) of each led for each beat of the music

data = myData.data  #read in each led value for each music beat

GPIOS=[13,14,15,16,17] #GPIOs used with leds
Leds=[Pin(i,Pin.OUT)  for i in GPIOS]  #initialize 5 leds for output

LEDS = 5  # number of leds
index=0  #index into data for state of each led
BPM = 122  # 122 beats per minute music track.  Used to set timer to sync
period = int(30000/BPM)  #how often timer fires to sync with music
    
def UpdateLeds(timer):  # reads led data with each music beat
    global index
    for ledNumber in range(LEDS):  # 5 leds to set with each beat
        Leds[ledNumber].value(data[index % len(data)]) # data loops continuously
        index+=1 
            
    
timer=Timer(-1)
timer.init(period=period, mode=Timer.PERIODIC, callback=UpdateLeds)   #initializing the timer, for music




