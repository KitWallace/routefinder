#!/usr/bin/env python

import time
import geo, convert
from gps import GPS
from persistant import get

class Track (object) :
   def __init__(self,name) :
      self.name = name
 
   def monitor(self, switch_name, rate_name) :
      file = open("log/"+self.name+".txt","a")
      while True :
         if get(switch_name).on :
           gps = get("gps")
           if gps.HDOP < 5.0 :   #  ignore low accuracy readings
              compass = get("compass")
              file.write( ",".join(("gps",gps.dateTime,str(round(gps.latitude,5)),str(round(gps.longitude,5)),str(gps.altitude),
                          str(gps.speedOverGround),str(gps.courseOverGround),str(compass.bearing) ,"\n")))
              file.flush()
         time.sleep(get(rate_name).value)

   def length(self) :
      last = None
      data = ()
      distance=0.0
      file = open("log/"+self.name+".txt","r")
      for line in file.readlines():
         if line == "":
            continue
         data = line.strip().split(",")
         if data[0] == "gps" :
            latitude = float(data[2])
            longitude = float(data[3])
            if last is None :
               last = geo.LatLong(latitude,longitude)
               start = data[1]
            else:
               next =  geo.LatLong(latitude,longitude)
               distance += last.gc_distance(next)
               last = next
               end = data[1]
      return (distance, start, end)
    
   def as_kml(self) :
       distance = convert.value(self.length()[0],"Nm","km")
       kml = "<Placemark><name>" + self.name + "</name>"
       kml += "<description>" + "Length along path " +  str(round(distance,2)) + " km" + "</description>"
       kml += "<LineString><altitudeMode>absolute</altitudeMode><coordinates>"
       file = open("log/"+self.name+".txt","r")
       for line in file.readlines():
          if line == "":
             continue
          data = line.strip().split(",")
          if data[0] == "gps" :
              latitude = data[2]
              longitude = data[3]
              altitude = data[4]
              coords =  ",".join((str(round(float(longitude),4)), str(round(float(latitude),4)) , str(round(float(altitude),4)) ))
              kml+=  coords + "\n"
       kml += "</coordinates></LineString>"
       kml += "</Placemark>"
       return kml

   def replay(self,interval_secs) :
       file = open("log/"+self.name+".txt","r")
       gps = get("gps")
       gps.HDOP = 1.5
#       compass = get("compass")
       for line in file.readlines():
          if line == "":
             continue
          data = line.strip().split(",")
          if data[0] == "gps" :
              gps.dateTime = data[1]
              gps.latitude = float(data[2])
              gps.longitude = float(data[3])
              gps. altitude = float(data[4] )
              gps.speedOverGround= float(data[5])
              gps.courseOverGround= float(data[6])
              gps.put()
#              compass.device_heading = float(data[7])
#              compass.put()
          time.sleep(interval_secs)
       file.close()
