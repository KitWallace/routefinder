#!/usr/bin/python

import time,sys
import weather_log
from config import Config
from persistant import get
from weather_log import Weather_Log

c = Config()
log = Weather_Log(c.weather_log_name,float(c.weather_log_rate))
log.monitor()

