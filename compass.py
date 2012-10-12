#!/usr/bin/env python

import time
from persistant import *
from Devantech_CMPS10 import CMPS10

class Compass(Persistant) :
   def __init__(self, name, declination = 0, offset = 0) :
       self.name = name
       self.device = CMPS10()
       self.declination = declination
       Number("compassoffset",offset)
       self.device_bearing = self.device.magnetic_bearing
       self.put()

   @property 
   def bearing(self) :
       return int(round (( self.device_bearing + self.declination - get("compassoffset").value  + 360) % 360, 0))
   
   def zero(self) :
       offset = get("compassoffset")
       offset.val = self.device_bearing
       offset.put()
       return self
      
   @property 
   def offset(self) :
       return get("compassoffset").value

   def update(self,period=1) :
       while True:
           self.device_bearing = self.device.magnetic_bearing
           self.put()
           time.sleep(period)

   def __getstate__(self) :
       odict = self.__dict__.copy()
       del odict['device']
       return odict
  
