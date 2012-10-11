#!/usr/bin/env python

from geo import *

class Track (object) :
   def __init__(self,name) :
      self.name = name
      self.file = open("log/"+self.name+".txt","r")

   def length(self) :
      last = None
      data = ()
      distance=0.0
      self.file = open("log/"+self.name+".txt","r")
      for line in self.file.readlines():
         if line == "":
           continue
         data = line.strip().split(",")
         latitude = float(data[1])
         longitude = float(data[2])
         if last is None :
             last = LatLong(latitude,longitude)
             start = data[0]
         else:
             next =  LatLong(latitude,longitude)
             distance += last.gc_distance(next)
             last = next
      end = data[0]
      return (distance, start, end)
    
   def as_kml(self) :
       distance = self.length()
       kml = "<Placemark><name>" + self.name + "</name>"
       kml += "<description>" + "Length along path " +  str(distance[0]) + " Nm" + "</description>"
       kml += "<LineString><altitudeMode>absolute</altitudeMode><coordinates>"
       self.file = open("log/"+self.name+".txt","r")
       for line in self.file.readlines():
          if line == "":
             continue
          data = line.strip().split(",")
          latitude = data[1]
          longitude = data[2]
          altitude = data[3]
          kml+=  str(round(float(longitude),4))  + "," + str(round(float(latitude),4)) +  "," + str(round(float(altitude),4)) + "\n"
       kml += "</coordinates></LineString>"
       kml += "</Placemark>"
       return kml
