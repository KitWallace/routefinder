#!/usr/bin/python

import time,sys
from persistant import *
import log
from config import Config
c = Config()

Switch("logsw")
Number("lograte",initial=float(c.log_rate),step=10)
log = log.Log(c.log_name)
log.monitor("logsw","lograte")

