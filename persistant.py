#!/usr/bin/env python

import pickle, time

def get(name) :   
      tries = 2
      while tries > 0 :
        try :
           file = open("obj/"+name+".pkl","rb")
           return pickle.load(file)
        except EOFError :
           time.sleep(0.02)
           tries-= 1

class Persistant(object) :
   
    def __init__(self,name) :
        self.set(name)
    
    def set(self,name) :
        self.name = name
        self.ts = time.time()
    
    def put(self) :
        file = open("obj/"+self.name+".pkl","wb")
        self.ts = time.time()
        pickle.dump(self,file)
        return self

    @property
    def ts_dateTime(self) :
        return time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(self.ts))

class Switch(Persistant) :
     
    def __init__(self,name) :
        self.name = name
        self.on = True
        self.put()
    
    def switch_on(self) :
        self.on= True
        self.put()
        return self

    def switch_off(self) :
        self.on= False
        self.put()
        return self
    
    def toggle(self) :
        self.on = not self.on
        self.put()
        return self

    @property
    def status(self) :
        if self.on is None :
            return "unset"
        elif self.on :
            return "on"
        else : 
            return "off"
                  
class Number(Persistant) :
    def __init__(self,name,initial=0,step=1,min=0, max=100000, wrap=False) :
      self.name = name
      self.initial = initial
      self.step = step
      self.min = min
      self.max = max
      self.val = self.initial
      self.wrap = wrap
      self.put()

    def increment(self,m=0) :
      if m==0 :
         m = self.step
      next = self.val + m
      
      if next > self.max :
           if self.wrap :
              self.val = self.min
           else :
              self.val= self.max
      else :
          self.val = next
      self.put()
      return self

    def decrement(self,m=0) :
      if m==0 :
         m = self.step
      next= self.val - m
      if next < self.min :
           if self.wrap :
              self.val = self.max
           else :
              self.val= self.min
      else :
          self.val = next
      self.put()
      return self
   
    @property
    def value(self) :
      return int(self.val)

class Option(Persistant) :
    def __init__(self,name,choices) :
      self.name = name
      self.choices = choices
      self.initial = 0
      self.step = 1
      self.min = 0
      self.max = len(choices) - 1
      self.val = 0
      self.wrap = True
      self.put()

    def increment(self,m=0) :
      if m==0 :
         m = self.step
      next = self.val + m
      
      if next > self.max :
           if self.wrap :
              self.val = self.min
           else :
              self.val= self.max
      else :
          self.val = next
      self.put()
      return self

    def decrement(self,m=0) :
      if m==0 :
         m = self.step
      next= self.val - m
      if next < self.min :
           if self.wrap :
              self.val = self.max
           else :
              self.val= self.min
      else :
          self.val = next
      self.put()
      return self
   
    @property
    def value(self) :
      return self.choices[self.val]

        
      

