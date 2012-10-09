#!/usr/bin/env python

import math 
points = ["N","NNE","NE","ENE","E","ESE","SE" ,"SSE" ,"S", "SSW","SW","WSW","W", "WNW","NW","NNW","N"]
R =  3437.74677   #nautical miles

# but wikipedia has the mean radius  3440.06479


def deg_to_dms(dd,latlong) :

   if (latlong == "lat"):
      if (dd< 0) :
         dir = "West"
      else :
         dir = "East"
   else :
      if (dd< 0) :
         dir = "South"
      else :
         dir = "North"

   dd = abs(dd)
   deg = int(dd)
   min = (dd - deg ) * 60
   dmin = int(min)
   sec = int((min - dmin) * 60)
   return "".join([str(deg)," degrees ", str(dmin), "minutes ",str(sec) , " seconds ", dir])

def degrees_to_compass_point(deg) :
   dp = deg + 11.25
   dp = dp % 360 
   dp = int(dp // 22.5)
   return points[dp] 

def degrees_to_hours(deg) :
   deg = deg + 15
   deg = deg % 360 
   hours = int(deg // 30)
   return hours if hours !=0 else 12


class LatLong(object) :
  def __init__ (self,lat,long) :
    self.latitude= lat
    self.longitude = long

  def gc_distance(self,p):
    """
    Calculate the great circle distance in nautical miles between this LatLong and another
    using the haversine formula and the initial bearing in degrees

    see http://en.wikipedia.org/wiki/Haversine_formula
    and http://www.movable-type.co.uk/scripts/latlong.html
    """
    lat1,lon1,lat2,lon2 = map(math.radians,[self.latitude,self.longitude,p.latitude,p.longitude])
    dlat = lat1 - lat2
    dlon = lon1 - lon2
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    nm = c * R
    return round(nm,6)

  def gc_bearing(self,p):
    """
    Calculate the great circle initial bearing in degrees
    """
    lat1,lon1,lat2,lon2 = map(math.radians,[self.latitude,self.longitude,p.latitude,p.longitude])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    y = math.sin(dlon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    bearing = math.degrees(math.atan2(y, x))
    bearing = (bearing + 360) % 360
    return bearing

  def gc_polar_to(self,p) :
    return PolarLocation( self.gc_distance(p), self.gc_bearing(p))

class PolarLocation(object) :
    def __init__(self, distance, bearing ):
       self.distance = distance
       self.bearing = bearing

if __name__ == "__main__" :

    for i in  range(0,36) :
       deg= i * 10
       print deg,degrees_to_compass_point(deg), degrees_to_hours(deg)

    p1 = LatLong (0,0)
    print p1.gc_distance(LatLong(0,1)), p1.gc_bearing(LatLong(0,1))
    print p1.gc_distance(LatLong(1,0)), p1.gc_bearing(LatLong(1,0))
    print p1.gc_distance(LatLong(0,-1)), p1.gc_bearing(LatLong(0,-1))
    print p1.gc_distance(LatLong(-1,0)), p1.gc_bearing(LatLong(-1,0))
 
    p1 = LatLong (51,-2)
    print p1.gc_distance(LatLong(51,-3)), p1.gc_bearing(LatLong(51,-3))
    print p1.gc_distance(LatLong(52,-2)), p1.gc_bearing(LatLong(52,-2))
    print p1.gc_distance(LatLong(51,-1)), p1.gc_bearing(LatLong(51,-1))
    print p1.gc_distance(LatLong(50,-2)), p1.gc_bearing(LatLong(50,-2))

