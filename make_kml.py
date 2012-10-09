#!/usr/bin/env python

from persistant import get
import log
import sys

name = sys.argv[1]
log = get(name)
kml = log.kml()
print kml
