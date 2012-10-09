#!/usr/bin/env python

conversions = {'kt': {'mph' : 1.15077945,'m/s':  0.514444444 ,"kph" : 1.85200 },  
               "mb" : {'hPa' : 1.0, "inchHg" :  29.529983071E-3},
               "Nm" : {"km" : 1.85200 ,"m" : 1852.00 , "miles" : 1.15078 }
              }


def convert_value(value, fromUnit, toUnit) :
    try :
        factor = conversions[fromUnit][toUnit]
        return value * factor
    except: 
        try :
           factor = conversions[toUnit][fromUnit]
           return value / factor
        except :
           return None

