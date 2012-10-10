#!/usr/bin/env python
import time
from persistant import *

class Log(Persistant) :
   def __init__(self,name) :
      self.name = name
      self.put()

   def log(self,message) :
      position = get("gps")
      file = open("log/"+self.name+".txt","a")
      file.write(str(position) + "," + str(message)+"\n")
      file.close()
      return message

   def monitor(self, switch_name,rate_name) :
      while True :
         if get(switch_name).on :
           position = get("gps")
           file = open("log/"+self.name+".txt","a")
           file.write(str(position)+"\n")
           file.close()
         time.sleep(get(rate_name).value)

