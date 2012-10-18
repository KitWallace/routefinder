#!/usr/bin/python
import time
import speak, convert
from persistant import *
from config import Config

c = Config()
# need some history  so we can switch even if we havent got to within min_proximity of the waypoint 
    
def follow(min_proximity,interval_secs,voice) :
   """ this does a simple follow of a route in serial order of the waypoints
       this detects 2 transitions:
           1. arrival - coming from a distance > proximity to within proximity
                 action - say arrival and the text 
           2. departure - changing from a distance < proximity to a distance > proximity
                 action - say new waypoint and distance

       start away from every waypoint
       anticipate problem with bouncing in and out at the periphery so make arrival proximity and departure proximity different 

   """

   inside = True
   while True :
      if get("follow_sw").on :
         route = get("route")
         current_wp = route.current_waypoint
         distance = current_wp.distance("km")
         if not inside and distance < min_proximity * 0.8  :     #  arrival
              text = "You are arriving at " + current_wp.name + ". " + current_wp.text
              speak.say(text,voice)
              inside = True
              print(text)
 
         elif inside and distance > min_proximity  :   # departure
              route.next     # move to next waypoint
              route.put()    # update
              next_wp = route.current_waypoint
              inside = False
              text = "Your next waypoint is " + next_wp.name + " which is " + str(round(next_wp.distance("km"),1))+ " km away."
              speak.say(text,voice)
              print(text)
      time.sleep(interval_secs)

sw = Switch("follow_sw")
sw.toggle()  # set it off 
follow(float(c.follow_proximity), float(c.follow_rate), c.follow_voice)

