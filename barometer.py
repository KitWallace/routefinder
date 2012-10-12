#!/usr/bin/python

import time, sys
from persistant import *
from Adafruit_BMP085 import BMP085
from moving_sequence import *
import weather

def baroReader(interval_secs,altitude) :
     baro = BMP085()
     while True :
          slbaro = round(baro.readSeaLevelPressure(altitude) / 100 ,2)
          yield(slbaro)
          time.sleep(interval_secs)

def baroSmoother(interval_secs,smooth_secs,altitude) :
    baro = baroReader(interval_secs,altitude)
    max = int(smooth_secs / interval_secs)
    while True:
       total_baro = 0.0
       for i in range(max) :
          reading = baro.next()
          total_baro += reading
       average_baro = round(total_baro / max, 2)
       yield(average_baro)
       

class Barometer(Persistant) :
    def __init__(self,name,interval_secs, smooth_secs, trend_secs,altitude) :
        self.name = name
        self.baro = None
        self.interval_secs = interval_secs
        self.smooth_secs = smooth_secs
        self.trend_secs = trend_secs 
        self.altitude = altitude
        self.trend_length = int(trend_secs /smooth_secs)
        self.history = Moving_Sequence(self.trend_length)
        self.trend = 0
        self.tendency = ""
        self.forecast = ""
        self.log = open("log/"+self.name+".txt","a")

    def monitor(self) :
        reader = baroSmoother(self.interval_secs,self.smooth_secs,self.altitude)
        for self.baro in reader :
            self.history.add(self.baro)
            self.updateTrend()
            self.put()
            self.log.write(", ".join((time.strftime("%Y-%m-%d %H:%M",time.localtime(self.ts)),str(self.baro),str(self.trend),self.tendency,self.forecast)) + "\n")
            self.log.flush()
 #           print time.strftime("%a %H:%M",time.localtime(self.ts)),self.baro,self.trend,self.tendency,self.forecast
 
    def updateTrend(self) :
        if self.history.get(-1) is not None :
            self.trend = self.history.get(0) - self.history.get(-1)
            self.tendency = weather.trend_to_tendency(self.trend)
            self.forecast = weather.forecast1(self.baro,self.trend)

    def talk_text(self) :
        return "Barometer is " + str(int(round(self.baro,0))) +  ", " + self.tendency + ". Forecast " + self.forecast
        
    def __getstate__(self) :
        odict = self.__dict__.copy()
        del odict['history']
        del odict['log']
        return odict
    
