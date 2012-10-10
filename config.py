#!/usr/bin/env python


class Config(object) :
   def __init__(self,name="config") :
      c = open("config/"+name + ".txt","r")
      for line in c.readlines() :
         line = line.strip()
         if line != ""  or line.startswith("#") :
            (parameter,value) = line.split("=")
            self.__dict__[parameter] = value

if __name__ == "__main__" :
   c = Config("test")
   print c.a
         
