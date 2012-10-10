#!/usr/bin/env python

from track import *
import sys
import convert

name = sys.argv[1]
track = Track(name)
#k ml = track.kml()
distance = track.track_length()

print distance, convert.convert_value(distance[0],"Nm","miles")
