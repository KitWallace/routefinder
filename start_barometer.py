#!/usr/bin/python

from barometer import *
from config import Config
c = Config()
      
baro = Barometer("baro",60,300,10800,float(c.barometer_altitude))
baro.monitor()

    
 
