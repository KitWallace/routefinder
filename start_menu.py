#!/usr/bin/python

import sys, time, termios
import speak

from menu import *
from persistant import *
from config import Config

c = Config()

def visit(item) :
   action = item.getAttribute('action')
   if action == "" :
      text = item.getAttribute('title')
   else : 
      text = eval(action)
   mtext = speak.expand(text,speak.tracker_substitutes)
   speak.say(mtext,c.menu_voice)
   print (text)
   
menu = Menu(c.menu)
menu.run(visit) 

