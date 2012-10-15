#!/usr/bin/python

import time,sys
from persistant import *
from track import Track
from config import Config

c = Config()
Switch("log_sw")
Number("log_rate",initial=float(c.position_log_rate),step=10)
track = Track(c.position_log_name)
track.monitor("log_sw","log_rate")

