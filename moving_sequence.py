#!/usr/bin/python

import time
class Moving_Sequence(object) :
    """ handle a moving sequence of objects
        the size of the sequence is limited
        objects are added at the beginning 
        implemented as a cyclic sequence

    """
    
    def __init__(self,limit) :
        self.limit = limit
        self.seq = [None for i in range(limit)]
        self.current = self.limit - 1

    def full(self) :
        return self.get(0) is not None and self.current == self.limit - 1

    def add(self,obj) :
        if obj is None :
            pass
        else :
            self.current = (self.current + 1) % self.limit
            self.seq[self.current] = obj

    def get(self,i) :
        index = (self.current - i ) % self.limit 
        return self.seq[index]

    def __str__(self) :
        return  "[" + ",".join([str(i) + ":" + str(self.get(i)) for i in range(self.limit) ]) + "]"

    def diff(self,start=0,n=-1) :
        """ diff successive values in a sub-sequence of n values starting from start

        """ 
        if n == -1 :
            n = self.limit   #cant provide self.limit as default 
        if self.get(start) is not None and self.get(n + start - 1) is not None : 
            sum = 0
            for i in range(n - 1) :
                 sum += self.get(i + start) - self.get( i + start + 1)
            return sum

