#!/usr/bin/python

import gps
position = gps.GPS("gps")
position.monitor("/dev/ttyUSB0")
