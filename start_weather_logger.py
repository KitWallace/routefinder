#!/usr/bin/python

import time,sys
import weather_log
from config import Config
from persistant import get

class Weather_Log() :
   def __init__(self,name) :
      self.logname= name
      self.file = open("log/"+self.logname+".txt","a")

   def monitor(self, interval_secs) :
      while True :
         baro = get("barometer")
         #  add weather forecasting here
         self.file.write( ",".join(("baro",baro.ts_dateTime,str(baro.pressure),str(baro.temperature))) +"\n")
         self.file.flush()
         time.sleep(interval_secs)

c = Config()
log = Weather_Log(c.weather_log_name)
log.monitor(float(c.weather_log_rate))

