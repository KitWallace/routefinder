#!/usr/bin/python
import time
from persistant import *
import speak

class Book() :
  def __init__(self, name) :
     self.name= name
     self.val=0
     file = open("texts/" + self.name + ".txt","r")
     self.max= len(file.readlines())-1
  
  @property
  def line(self) :
     file = open("texts/" + self.name + ".txt","r")
     try :
       line = file.readlines()[self.val]
       line = line.replace("'","")
       return line
     except :
       return None

  @property
  def next(self) :
     self.val +=1 
     if self.val > max :
       self.val = self.max
     return self

  @property
  def previous(self) :
     self.val -=1 
     if self.val < 0 :
       self.val = 0
     return self

  @property
  def first(self) :
     self.val = 0 
     return self

class Library(Persistant) :
   def __init__(self,books,name="library") :
      self.name=name
      self.books = []
      for book in books.split(",") :
          self.books.append(Book(book))
      self.wrap  = True
      self.min = 0
      self.max = len(self.books) - 1
      self.val = 0
      self.put()

   @property 
   def current_book(self) :
      return self.books[self.val]

   def set_current(self, abook) : 
       i=0  
       for book in self.books :
           if abook.name == book.name :
              self.val = i
           i+= 1
       self.put()
       return self.current_book

   @property
   def next(self) :
      next = self.val + 1   
      if next > self.max :
           if self.wrap :
              self.val = self.min
           else :
              self.val= self.max
      else :
          self.val = next

      return self.books[self.val]

   @property
   def previous(self) :
      next= self.val - 1
      if next < self.min :
           if self.wrap :
              self.val = self.max
           else :
              self.val= self.min
      else :
          self.val = next 

      return self.books[self.val]

   def start(self) :
      self.current_book.first
      line = self.current_book.nextline()
      self.put()
      return line

   def previousline(self) :
      line = self.current_book.previous.line
      self.current_book.next
      self.put()
      return line

   def nextline(self) :
      line = self.current_book.line
      self.current_book.next
      self.put()
      return line

   def firstline(self) :
      line = self.current_book.first.line
      self.current_book.next
      self.put()
      return line

   def read(self,interval_secs,voice) :
      while True :
        if get("read_sw").on :
           line = self.nextline()
           speak.say(line,voice)
           print line
        time.sleep(float(interval_secs))

if __name__ == "__main__" :
   l = Library("blackbox,rjam")

   b = l.current_book
   print b.line
   print b.next.line
   print l.next.line
