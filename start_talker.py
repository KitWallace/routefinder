#!/usr/bin/python

import time,sys
import speak,date_time
from persistant import *
from config import Config

c = Config()
Number("talk_rate",step=10,initial=float(c.talk_rate))
Switch("talk_sw")
Option("talk_mode",["location","velocity","time","relative location","relative velocity","expected time of arrival"])

if c.talk_status == "off" :
   Switch("talk_sw").toggle()

while True :
   if get("talk_sw").on :
      mode = get("talk_mode").value
      if mode == "location" :
          string = get("gps").location
      elif mode== "velocity" :
          string = get("gps").velocity    
      elif mode == "relative location" :
          destination = get("route").current_waypoint
          string = destination.relative_location
      elif mode == "relative velocity" :
          destination = get("route").current_waypoint
          string = destination.relative_velocity
      elif mode == "expected time of arrival" :
          destination = get("route").current_waypoint
          string = destination.eta
      elif mode == "time" :
          string = date_time.say_time()
      else :
          pass
      mstring = speak.expand(string,speak.tracker_substitutes)
      speak.say(mstring,c.talk_voice)
      print string
   time.sleep(get("talk_rate").value)
