#!/usr/bin/env python

from geo import *

class Track (object) :
   def __init__(self,name) :
      self.name = name
      self.file = open("log/"+self.name+".txt","r")

   def track_length(self) :
      last = None
      data = ()
      distance=0.0
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
    
   def kml(self) :
      kml=  "<kml xmlns='http://www.opengis.net/kml/2.2'><Folder><name>"+self.name+"</name>\n"
      for line in self.file.readlines():
         if line == "":
           continue
         data = line.strip().split(",")
         ts = data[0]
         (date,time) = ts.split("T")
         latitude = data[1]
         longitude = data[2]
         altitude = data[3]
         sog = data[4]
         cog = data[5]
         kml+= "<Placemark>"

         kml+= "<description>" + time[0:5] + " " + str(round(float(latitude),4)) + "," + str(round(float(longitude),4))  + "</description>\n"

         kml+= "<TimeStamp><when>"+ts+"</when></TimeStamp>\n"
         kml+= "<Point><coordinates>" + longitude + "," + latitude + "," + altitude+"</coordinates></Point>\n"
         kml+= "</Placemark>\n"
      kml+="</Folder></kml>\n"
      return kml
