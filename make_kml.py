#!/usr/bin/env python

import sys
from route import *
from track import *

routename = sys.argv[1]
trackname = sys.argv[2]
track = Track(trackname)
route = Route(routename)

kml = "<kml xmlns='http://www.opengis.net/kml/2.2'><Folder>\n"
kml += track.as_kml()
kml += route.as_kml()
kml += "</Folder></kml>"
print kml
