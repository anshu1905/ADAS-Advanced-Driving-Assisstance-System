import os
import time
import playsound
import serial #Import Serial Library
import time

from pygame import mixer
mixer.init()
sound = mixer.Sound('alarm.wav')

arduinoSerialData = serial.Serial('COM10',9600) #Create Serial port object called arduinoSerialData

l=[]
while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        myData_float=float(myData)
        if myData_float<50:
            try:
                sound.play()
            except:
                pass
            
        l.append(float(myData_float))
        
