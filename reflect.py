class Reflect:
 """ An object that use reflection """

 def __init__(self,obj):
  """ the constructor of this object """
  self.obj = obj

 def print_methods(self):
  """ print all the methods of this object and their doc string"""
  print '\n* Methods *'
  for name in dir(self.obj):
   attr = getattr(self.obj,name)
   if callable(attr) and not (name[0:2] == "__"):
    print name,':',attr.__doc__

 def print_attributes(self):
  """ print all the attributes of this object and their value """
  print '* Attributes *'
  for name in dir(self.obj):
   attr = getattr(self.obj,name)
   if not callable(attr) and not (name[0:2] == "__"):
    print name,':',attr

 def print_all(self):
  """ calls all the methods of this object """
  self.print_attributes()
  self.print_methods()
 
