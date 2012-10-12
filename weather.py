#!/usr/bin/python

tendency_table = \
  (   
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

forecast1_table = \
  (
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
    if trend is not None :
        return find(tendency_table,trend)

def forecast1 (baro, trend) :
    if baro is not None and trend is not None :
        return find(find(forecast1_table,baro),trend)



