#!/usr/bin/python

import time, sys
from persistant import *
from Adafruit_BMP085 import BMP085

class Barometer(Persistant) :
   def __init__(self,interval_secs,altitude) :
     self.name="barometer"
     self.baro = BMP085()
     self.interval_secs = interval_secs
     self.altitude = altitude
     self.pressure = None
     self.temperature = None
   
   def monitor (self) :
     while True :
          self.pressure = round(self.baro.readSeaLevelPressure(self.altitude) / 100 ,2)
          self.temperature = self.baro.readTemperature()
          self.put()
          time.sleep(self.interval_secs)

   def __getstate__(self) :
        odict = self.__dict__.copy()
        del odict['baro']
        return odict
    
