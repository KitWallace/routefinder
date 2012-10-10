#!/usr/bin/env python

import convert
from persistant import *
from geo import *

class Waypoint(Persistant) :
   def __init__(self,name,latitude,longitude,text="") :
     self.name = name
     self.latlong = LatLong(latitude,longitude)
     self.text = text

   @property
   def location(self) :
      gps = get("gps") 
      compass = get("compass")

      polar_to_waypoint = gps.latlong.gc_polar_to(self.latlong) 
      waypoint_bearing = int(round(polar_to_waypoint.bearing,0))
      relative_bearing = int(round((waypoint_bearing - compass.bearing + 360 ) % 360, 0))
      distance = round(convert.convert_value(polar_to_waypoint.distance,"Nm","km"),1)
      if distance > 1 :
          dtext =str(distance) + " km"
      else :
          dtext = str(int(round(convert.convert_value(distance,"km","m"),0))) + " m"
      dest_text = ( self.name + " is " + dtext + " away " +  str(waypoint_bearing) + " degrees." 
                   + " " + str(degrees_to_hours(relative_bearing)) + " oclock " )
      return dest_text

   @property
   def speed_and_direction (self) :
      gps = get("gps") 
      speed = round(convert.convert_value(gps.speedOverGround,"kt","kph"),1)
      course = int(gps.courseOverGround)
      points = degrees_to_compass_point(course)
      speed_text = "Going " + points + " at " + str(speed) + " kph "
      return speed_text

   @property
   def relative_speed_and_direction(self) :
      gps = get("gps") 
      compass = get("compass")
      polar_to_waypoint = gps.latlong.gc_polar_to(self.latlong) 
      waypoint_bearing = int(round(polar_to_waypoint.bearing,0))
      relative_bearing = (waypoint_bearing - gps.courseOverGround + 360 ) % 360
      distance = round(polar_to_waypoint.distance,2)  
      speed = round(convert.convert_value(gps.speedOverGround,"kt","kph"),1)

      if relative_bearing > 270 or relative_bearing < 90 :
          dir = "toward"
      else :
          dir = "away from"
      vmg = round(speed * math.cos(math.radians(relative_bearing)),1)
      course = int(gps.courseOverGround)
      if vmg != 0.0 :
          vmg_text= "you are moving "+ dir + " " + self.name + " at " + str(abs(vmg)) + " kph " + " relative bearing " + str(relative_bearing)
          if dir == "toward" :
              hours = round(distance / vmg,2)
              if hours < 1.0 :
                  minutes = int(round(hours * 60 ,0))
                  vmg_text += ". Arrival in " + str(minutes) + " minutes time."
              else :
                 vmg_text += ". Arrival in " + str(hours) + " hours time."
      else :
          vmg_text = "you are stationary."
      return vmg_text

class Route(Number) :
   def __init__(self,name) :
     self.name = "route"
     waypointFile = open("routes/" + name + ".txt","r")
     self.waypoints = [] 
     for line in waypointFile.readlines() :
        line = line.strip()
        if line != "" :
           (name,latitude,longitude,text) = line.split("|")
           waypoint = Waypoint(name,float(latitude),float(longitude),text)
           self.waypoints.append(waypoint)

     self.wrap  = True
     self.initial = 0
     self.min=0
     self.max = len(self.waypoints) - 1
     self.val = 0
     self.put()

   @property
   def current_waypoint(self) :
       return self.waypoints[self.value]


if __name__ == "__main__" :
   route = Route("box")
   for waypoint in route.waypoints :
      print waypoint.location

   print route.current_waypoint.location 
   print route.current_waypoint.speed_and_direction
   print route.current_waypoint.relative_speed_and_direction


