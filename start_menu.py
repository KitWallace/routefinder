#!/usr/bin/env python

import sys, time, termios
import speak

from menu import *
from persistant import *

def visit(item) :
   action = item.getAttribute('action')
   if action == "" :
      text = item.getAttribute('title')
   else : 
      text = eval(action)
   mtext = speak.expand(text,speak.tracker_substitutes)
   speak.say(mtext)
   print (text)
   
name = sys.argv[1]
menu = Menu(name)
menu.run(visit) 

