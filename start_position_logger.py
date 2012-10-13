#!/usr/bin/python

import time,sys
from persistant import *
from track import Track
from config import Config

Switch("logsw")
Number("lograte",initial=float(c.position_log_rate),step=10)

c = Config()
track = Track(c.position_log_name)
track.monitor("logsw","lograte")

