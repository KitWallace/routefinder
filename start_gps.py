#!/usr/bin/python

import gps
position = gps.GPS("gps")
position.update("/dev/ttyUSB0")
