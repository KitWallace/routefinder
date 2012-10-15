#!/usr/bin/python
import time
from persistant import *

tendency_table = (
    (6.05,"rising very rapidly"),
    (3.55 , "rising quickly"),
    (1.55 , "rising"),
    (0.1 , "rising slowly"),
    (-0.1 , "steady"),
    (-1.55 , "falling slowly"),
    (-3.55, "falling"),
    (-6.05 , "falling quickly"),
    (-99 , "falling very rapidly")
  )

forecast1_table =   (
    (1022, ( (-0.1 , "Continued fair"),
             (-1.55 , "Fair") ,
             (-99 , "Cloudy, Warmer")
           )
    ),
    (1009, ( (-0.1 , "Same as present"), 
             (-1.55 , "Little change"), 
             (-99 , "Precipitation likely")
           ) 
    ),
    (0 , ( (-0.1 , "Clearing, cooler"),
             (-1.55 , "Precipitation"), 
             (-99 , "Storm")
           ) 
    )
)

def find(table,myval) :
    for threshold,value in table :
        if myval >= threshold :
           return value

def trend_to_tendency(trend) :
    return find(tendency_table,trend)

def sc_forecast(pressure, trend) :
    # http://www.sciencecompany.com/-W135.aspx
    return find(find(forecast1_table,pressure),trend)


class Weather_Log(Persistant) :
   def __init__(self,logname="weather",interval_secs=60,name="weather") :
      self.name=name
      self.logname= logname
      self.interval_secs = interval_secs
      self.put()

   def monitor(self) :
      self.file = open("log/"+self.logname+".txt","a")
      while True :
         baro = get("barometer")
         self.file.write( ",".join(("baro",baro.ts_dateTime,str(baro.pressure),str(baro.temperature) )) +"\n")
         self.file.flush()
         time.sleep(self.interval_secs)

   def past_pressure(self,n) :
      try :
         file = open("log/"+self.logname+".txt","r")
         lines = file.readlines()
         line = lines[-n]
         data = line.split(",")
         pressure = float(data[2])
         return pressure
      except :
         return None

   def pressure(self) :
      return get("barometer").pressure

   def trend(self, hours) :
      past_pressure = self.past_pressure(int(3600 * hours / self.interval_secs))
      if past_pressure is not None :
            return past_pressure - self.pressure()

   def forecast(self) :
     trend = self.trend(3)
     if trend is not None :
        pressure = self.pressure()
        return sc_forecast(pressure,trend)

   def tendency(self,hours) :
     trend = self.trend(hours)
     if trend is not None :
        return trend_to_tendency(trend)

   def say_pressure(self) :
     return str(int(round(self.pressure(),0))) + " mb " + self.say_tendency()

   def say_tendency(self) :
     trend = self.trend(3)
     if trend is not None :
        return trend_to_tendency(trend) + " Change is " + str(round(trend,1)) + " mb in the past 3 hours "
           
if __name__ == "__main__" :
   weather = Weather_Log("weather",60,"test")
   print weather.pressure()
   print weather.past_pressure(5)
   print weather.past_pressure(180)
   print weather.trend(1)
   print weather.trend(3)
   print weather.tendency(3)
   print weather.say_tendency()
   print weather.say_pressure()
   print weather.forecast()
