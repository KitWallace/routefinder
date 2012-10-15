#!/usr/bin/python

import datetime, time
import moon

def datetime_from_xs(xdt) :
   return datetime.datetime.strptime(xdt,"%Y-%m-%dT%H:%M:%S")

def seconds_to_go(xdt) :
    # in seconds
    dt  = datetime_from_xs(xdt)
    now = datetime.datetime.utcnow()
    diff = dt - now
    return diff.total_seconds()

def time_to_go(xdt) :
    total_seconds = seconds_to_go(xdt)
    seconds = int(total_seconds % 60)
    string = (str(seconds) + " seconds " if seconds > 0 else "")
    total_minutes = (total_seconds - seconds) / 60
    minutes = int(total_minutes % 60)
    string = (str(minutes) + " minutes " if minutes > 0 else "") + string
    total_hours = (total_minutes - minutes ) / 60
    hours = int(total_hours % 24)
    string =  (str(hours) + " hours " if hours > 0 else "" ) + string
    days = int((total_hours - hours) /24)
    string =  (str(days) + " days " if days > 0 else "") + string
    return string

def string(xdt) :
    dt = datetime_from_xs(xdt) 
    return dt.strftime("%B %d at %H %M")

def say(xdt) :
    dt = datetime_from_xs(xdt) 
    return dt.strftime("%B %d at %H %M")

def say_date() :
    day =int(time.strftime("%d"))
    return time.strftime("%A %B ") + str(day)

def say_time() :
    t = time.localtime()
    hours = t.tm_hour
    minutes = t.tm_min

    if minutes > 30 :
       hours += 1

    if hours <= 12 :
       hours_str = str(hours) + " a.m."
    elif hours > 12 :
       hours_str = str(hours - 12) + " p.m."
    string = (
          hours_str + " precisely " if minutes == 0 else 
          "a quarter past " + hours_str  if minutes == 15 else 
          "half past " + hours_str if minutes == 30 else 
          str(minutes) + " minute" + ("s" if minutes > 1 else "") + " past " + hours_str if minutes < 30 else 
          "a quarter to " + hours_str if minutes == 45 else 
          str(60 - minutes) + " minute" + ("s" if (60 - minutes) > 1 else "") + " to " + hours_str )

    return string
def say_moon_phase() :
    m = moon.MoonPhase()
    return ("""The moon is %s, %.1f%% illuminated, %.1f days old.""" %
        (m.phase_text, m.illuminated * 100, m.age))

if __name__ == "__main__" :
    dt = "2012-10-17T18:30:00"
    print datetime_from_xs(dt)
    print seconds_to_go(dt)
    print time_to_go(dt)
    print string(dt)
    print say_date()
    print say_time()
    print say_moon_phase()
