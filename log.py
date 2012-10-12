#!/usr/bin/env python
import time
from persistant import *

class Log(Persistant) :
   def __init__(self,name) :
      self.name = "log"
      self.logname= name
      self.put()

   def log(self,message) :
      position = get("gps")
      file = open("log/"+self.logname+".txt","a")
      file.write("msg,"+str(position) + "," + str(message)+"\n")
      file.close()
      return message

   def monitor(self, switch_name,rate_name) :
      while True :
         if get(switch_name).on :
           gps = get("gps")
           if gps.HDOP < 5.0 :   #  ignore low accuracy readings
              file = open("log/"+self.logname+".txt","a")
              file.write("gps,"+str(gps)+"\n")
              file.close()
         time.sleep(get(rate_name).value)

