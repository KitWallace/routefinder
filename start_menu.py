#!/usr/bin/python

import time, date_time
import speak
from menu import Menu
from persistant import get
from config import Config

c = Config()

def visit(item) :
   action = item.getAttribute('action')
   if action == "" :
      text = item.getAttribute('title')
   else : 
      text = eval(action)
   if text is not None :
      mtext = speak.expand(text,speak.tracker_substitutes)
      speak.say(mtext,c.menu_voice,c.menu_speed)
      print (text)
   
menu = Menu(c.menu)
menu.run(visit) 

