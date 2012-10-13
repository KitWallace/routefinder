#!/usr/bin/python

from barometer import *
from config import Config
c = Config()
      
baro = Barometer(int(c.barometer_update_rate),float(c.barometer_altitude))
print "Barometer started"
baro.monitor()

    
 
