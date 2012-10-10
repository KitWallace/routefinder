#!/usr/bin/env python
import time,sys

import speak
from persistant import *
from config import Config
c = Config()
Number("positiontalkrate",step=10,initial=float(c.talk_rate))
Switch("positiontalksw")
if c.talk_status == "off" :
   Switch("positiontalksw").toggle()

while True :
   if get("positiontalksw").on :
      gps = get("gps")
      destination = get("route").current_waypoint
      text = destination.location
      mtext = speak.expand(text,speak.tracker_substitutes)
      speak.say(mtext)
      print text
   time.sleep(get("positiontalkrate").value)
