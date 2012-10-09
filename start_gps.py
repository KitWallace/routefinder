#!/usr/bin/env python

import gps
position = gps.GPS("gps")
position.update("/dev/ttyUSB0")
