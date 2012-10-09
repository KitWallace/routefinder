#!/usr/bin/env python

import math, serial
from persistant import *
from geo import LatLong

class GPS(Persistant) :

  def __init__(self,name,latitude=0.0,longitude=0.0,altitude=0.0) :
    self.name=name
    self.latitude = latitude
    self.longitude = longitude
    self.altitude = altitude
    self.courseOverGround = 0.0
    self.speedOverGround = 0.0
    self.HDOP = 0.0
    self.satellites = 0
    self.dateTime= ""
    self.put()

  def update_with_RMC(self, sent) :
    data= sent.split(",")
    try :
      lat=data[3]
      latd=lat[0:2]
      latm=lat[2:]
      lat_dir = 1
      if data[4] == "S" :
        lat_dir = -1
      latitude = (int(latd) + float(latm) / 60) * lat_dir

      long=data[5]
      longd=long[0:3]
      longm=long[3:]
      long_dir = 1
      if data[6] == "W" :
        long_dir = -1
      longitude = (int(longd) + float(longm) / 60) * long_dir

      time =data[1]
      h = time[0:2]
      m = time[2:4]
      s = time[4:len(time)]
    
      date= data[9]
      day = date[0:2]
      month = date[2:4]
      year = date[4:6]
      dateTime = "-".join(("20"+year,month,day)) + "T" + ":".join((h,m,s))

      sog = float(data[7])
      cog = float(data[8])
      # all conversion done with no error

      self.latitude = latitude
      self.longitude = longitude
      self.dateTime = dateTime
      self.speedOverGround = sog
      self.courseOverGround = cog 
    except :
       pass
    return self

  def update_with_GGA(self, sent) :
    data = sent.split(",")
    self.altitude = data[9]
    self.satellites = data[7]
    self.HDOP = data[8]
    return self

  def update(self,port) :   
    s = serial.Serial(port,4800)
    while True:
       nmea = s.readline()
       if nmea.startswith("$GPRMC") :
         self.update_with_RMC(nmea)
         self.put()
       elif nmea.startswith("$GPGGA") :
         self.update_with_GGA(nmea)

  @property
  def latlong(self) :
    return LatLong(self.latitude,self.longitude)

  def __str__(self) :
    return ",".join((self.dateTime,str(round(self.latitude,5)),str(round(self.longitude,5)),str(self.altitude),
         str(self.speedOverGround),str(self.courseOverGround)))

 
