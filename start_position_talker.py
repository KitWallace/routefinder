#!/usr/bin/python

import time,sys
import speak
from persistant import *
from config import Config

c = Config()
Number("positiontalkrate",step=10,initial=float(c.position_talk_rate))
Switch("positiontalksw")
if c.position_talk_status == "off" :
   Switch("positiontalksw").toggle()

while True :
   if get("positiontalksw").on :
      gps = get("gps")
      destination = get("route").current_waypoint
      text = destination.location
      mtext = speak.expand(text,speak.tracker_substitutes)
      speak.say(mtext,c.position_talk_voice)
      print text
   time.sleep(get("positiontalkrate").value)
