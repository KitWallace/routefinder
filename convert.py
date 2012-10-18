#!/usr/bin/python

conversions = {'kt':  {"kt" : 1.0 ,"mph" : 1.15077945,'mps':  0.514444444 ,"kph" : 1.85200 },  
               "mb" : {"mb" : 1.0, "hPa" : 1.0, "inchHg" :  29.529983071E-3},
               "Nm" : {"Nm" : 1.0 , "km" : 1.85200 ,"m" : 1852.00 , "miles" : 1.15078 },
               "km" : {"km" : 1.0 , "m" : 1000}
              }


def value(value, fromUnit, toUnit) :
    try :
        factor = conversions[fromUnit][toUnit]
        return value * factor
    except: 
        try :
           factor = conversions[toUnit][fromUnit]
           return value / factor
        except :
           return None

