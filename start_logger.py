#!/usr/bin/env python
import time,sys
from persistant import *
import log

trackname = sys.argv[1]
Switch("logsw")
Number("lograte",initial=60,step=10)
log = log.Log(trackname)
log.monitor("logsw","lograte")

