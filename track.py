#!/usr/bin/env python

import geo, convert

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
       kml += "<description>" + "Length along path " +  str(distance) + " km" + "</description>"
       kml += "<LineString><altitudeMode>absolute</altitudeMode><coordinates>"
       self.file = open("log/"+self.name+".txt","r")
       for line in self.file.readlines():
          if line == "":
             continue
          data = line.strip().split(",")
          if data[0] == "gps" :
              latitude = data[2]
              longitude = data[3]
              altitude = data[4]
              coords =  str(round(float(longitude),4))  + "," + str(round(float(latitude),4)) +  "," + str(round(float(altitude),4))
              kml+=  coords + "\n"
       kml += "</coordinates></LineString>"
       kml += "</Placemark>"
       return kml
