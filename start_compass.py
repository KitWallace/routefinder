#!/usr/bin/python
from persistant import *
import compass
from config import Config
c = Config()
compass = compass.Compass("compass",float(c.compass_deviation))
compass.update(float(c.compass_update_rate))

    
