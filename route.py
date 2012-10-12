#!/usr/bin/env python
import math
import date_time,convert,geo
from persistant import *

class Waypoint(Persistant) :
   def __init__(self,name,latitude,longitude,datetime,text="") :
     self.name = name
     self.latitude = latitude
     self.longitude = longitude
     if datetime != "" :
         self.datetime = datetime
     else :
         self.datetime = None
     self.text = text

   @property
   def latlong(self) :
     return geo.LatLong(self.latitude,self.longitude)

   @property
   def location(self) :
      string =  (" latitude " + str(round(self.latitude,4)) + (" North " if self.latitude > 0 else " South " ) +
      " , longitude "+ str(round(self.longitude,4)) + (" East " if self.longitude > 0 else " West " ))
      return string

   @property
   def distance(self) :
      gps = get("gps") 
      return gps.latlong.gc_polar_to(self.latlong).distance 

   @property 
   def time_to_go(self) :
       if self.datetime is None :
           return ""
       else :
           return " in " + date_time.time_to_go(self.datetime) + " time."

   @property
   def relative_location(self) :
      gps = get("gps") 
      compass = get("compass")

      polar_to_waypoint = gps.latlong.gc_polar_to(self.latlong) 
      waypoint_bearing = int(round(polar_to_waypoint.bearing,0))
      relative_bearing = int(round((waypoint_bearing - compass.bearing + 360 ) % 360, 0))
      distance = round(convert.value(polar_to_waypoint.distance,"Nm","km"),1)
      if distance > 1 :
          string =str(distance) + " km"
      else :
          string = str(int(round(convert.value(distance,"km","m"),0))) + " m"
      string = self.name + " is " + string + " away " +  geo.degrees_to_compass_point(waypoint_bearing) + ". "
      string += " The Relative bearing is " + str(geo.degrees_to_hours(relative_bearing)) + " oh clock "     
      return string

   @property
   def relative_velocity(self) :
      gps = get("gps") 
      polar_to_waypoint = gps.latlong.gc_polar_to(self.latlong) 
      waypoint_bearing = int(round(polar_to_waypoint.bearing,0))
      relative_bearing = (waypoint_bearing - gps.courseOverGround + 360 ) % 360
      distance = round(polar_to_waypoint.distance,2)  
      speed = round(convert.value(gps.speedOverGround,"kt","kph"),1)

      if relative_bearing > 270 or relative_bearing < 90 :
          dir = "toward"
      else :
          dir = "away from"
      vmg = round(speed * math.cos(math.radians(relative_bearing)),1)
      course = int(gps.courseOverGround)
      if vmg != 0.0 :
          vmg_text= "you are moving "+ dir + " " + self.name + " at " + str(abs(vmg)) + " kph " + " relative bearing " + str(int(round(relative_bearing,0)))
      else :
          vmg_text = "you are stationary."
      return vmg_text          

   @property
   def eta(self) :
      gps = get("gps") 
      polar_to_waypoint = gps.latlong.gc_polar_to(self.latlong) 
      waypoint_bearing = int(round(polar_to_waypoint.bearing,0))
      relative_bearing = (waypoint_bearing - gps.courseOverGround + 360 ) % 360
      distance = round(polar_to_waypoint.distance,2)  
      speed = round(convert.value(gps.speedOverGround,"kt","kph"),1)
      string = ""
      if relative_bearing > 270 or relative_bearing < 90 :
          dir = "toward"
      else :
          dir = "away from"
      vmg = round(speed * math.cos(math.radians(relative_bearing)),1)
      course = int(gps.courseOverGround)
      
      if vmg != 0.0 :
          
          if dir == "toward" :
              hours = round(distance / vmg,2)
              if hours < 1.0 :
                  minutes = int(round(hours * 60 ,0))
                  string += " Arrival in " + str(minutes) + " minutes time."
              else :
                 string += " Arrival in " + str(hours) + " hours time."
      else :
          string += "you are stationary."
     
      if self.datetime is not None :
          string += " Due in " + date_time.time_to_go(self.datetime) + " time."

      return string         
           
   def as_kml(self) : 
         kml = "<Placemark><name>"+ self.name + "</name>\n"
         kml+= ("<description>" + self.text  +  "<br/>" + str(self.latitude)+","+ str(self.longitude) + " " +  
                (date_time.string(self.datetime) if (self.datetime is not None) else "") + "</description>\n" )
         kml+= "<Point><coordinates>"+ str(self.longitude) + "," + str(self.latitude) + ",0" + "</coordinates></Point>\n"
         kml+= "</Placemark>\n"  
         return kml

class Route(Persistant) :
   def __init__(self,name) :
     self.name = "route"
     waypointFile = open("routes/" + name + ".txt","r")
     self.waypoints = [] 
     for line in waypointFile.readlines() :
        line = line.strip()
        if line != "" :
           (name,latitude,longitude,datetime,text) = line.split("|")
           waypoint = Waypoint(name,float(latitude),float(longitude),datetime.strip(),text)
           self.waypoints.append(waypoint)

     self.wrap  = True
     self.min = 0
     self.max = len(self.waypoints) - 1
     self.val = 0
     self.put()

   def as_kml(self) : 
     kml="<Folder><name>" + self.name +"</name>"
     for waypoint in self.waypoints :
        kml+= waypoint.as_kml()
     kml+= "</Folder>"
     return kml

   @property 
   def current_waypoint(self) :
     return self.waypoints[self.val]

   def set_current(self, waypoint) : 
       i=0  
       for wp in self.waypoints :
           if wp.name == waypoint.name :
              self.val = i
           i+= 1
       self.put()
       return self.current_waypoint

   @property
   def next(self) :
      next = self.val + 1   
      if next > self.max :
           if self.wrap :
              self.val = self.min
           else :
              self.val= self.max
      else :
          self.val = next

      return self.waypoints[self.val]

   @property
   def previous(self) :
      next= self.val - 1
      if next < self.min :
           if self.wrap :
              self.val = self.max
           else :
              self.val= self.min
      else :
          self.val = next 

      return self.waypoints[self.val]

   @property
   def first(self) :
      self.val = self.min
      return self.waypoints[self.val]
    
   @property
   def last(self) :
      self.val = self.max
      return self.waypoints[self.val]

   @property
   def nearest(self) :
      gps = get("gps") 
      min = 99999
      nearest = None
      for waypoint in self.waypoints :
          distance = gps.latlong.gc_polar_to(waypoint.latlong).distance
          if distance < min :
             nearest = waypoint
             min = distance
      return nearest

   @property
   def earliest(self) :
      min = 10E10
      earliest = None
      for waypoint in self.waypoints :
          if waypoint.datetime is not None :
             seconds_to_go = date_time.seconds_to_go(waypoint.datetime)
             if seconds_to_go < min :
                earliest = waypoint
                min = seconds_to_go
      
      return earliest 

if __name__ == "__main__" :
   route = Route("hackspace")
   for waypoint in route.waypoints :
      print waypoint.relative_location

   print route.first.relative_location 
   print route.first.relative_velocity

   print route.last.string
   print route.last.time_to_go
   print date_time.datetime_from_xs(route.last.datetime)

   print route.nearest.name, route.nearest.distance
   print route.earliest.name, route.earliest.datetime
 
   route.set_current(route.earliest)
   print route.current_waypoint.name
   print route.current_waypoint.eta
