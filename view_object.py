#!/usr/bin/env python

from reflect import *
from persistant import get
import sys

name = sys.argv[1]
obj = get(name)
reflect = Reflect(obj)
print name
reflect.print_attributes()
