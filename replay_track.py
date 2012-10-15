#!/usr/bin/python
import sys
from track import Track
import gps,compass
import config

c= config.Config()
track = Track(c.position_log_name)
gps.GPS("gps")
compass.Compass("compass",c.compass_deviation)
track.replay(float(c.position_log_rate))
