# Raspberry PI talking route finder 

## Hardware

* Raspberry PI : Model B Revision 1.0  (from /proc/cpuinfo)
* Barometer : BMP085 breakout board from Sparkfun (via SKPang) http://www.skpang.co.uk/catalog/barometric-pressure-sensor-bmp085-breakout-p-712.html
* GPS : GlobalSat BU 353     http://www.globalsat.co.uk/product_pages/product_bu353.htm
* Compass : CMPS10 board from Devantech (Robot Electronics)  http://www.robot-electronics.co.uk/htm/cmps10doc.htm
* PiCobbler : http://www.skpang.co.uk/catalog/adafruit-pi-cobbler-breakout-kit-for-raspberry-pi-p-1125.html
* Anker 10000 mAh battery pack http://www.ianker.com/Anker-Astro-10000mAh-External-battery-External%20Baterry/goods-43.html?&cat_id=17&line_id=114
* Labtec Powerpoint Presenter http://www.labtec.com/index.cfm/gear/details/EUR/EN,crid=29,contentid=730

## Unix Software
* Debian wheezy/sid   (via /etc/issue)
* Raspberry  Pi reference 2012-07-15 (via /etc/rpi-issue)
* Firmware version :  Aug 25 2012  version 333349  (via sudo /opt/vc/bin/vcgencmd version)  
* espeak  text to Speech
* python 2.7

### added kernel modules
* i2C-bcm2700
* i2c-dev

### Unix configuration

* audio out to audio jack

## Python Packages
### standard
sys
time
datetime
math
serial

### imported
* Adafruit_I2c.py   the Adafruit I2C API
* moon.py  - modified version of  http://bazaar.launchpad.net/~keturn/py-moon-phase/trunk/annotate/head:/moon.py  by Kevin Turner <acapnotic@twistedmatrix.com>  based on work by John Walker http://www.fourmilab.ch/ based on algorithm by Peter Duffett-Smith "Practical Astronomy With Your Calculator


## Project code

### Reflection
- reflect.py  - defines a Reflect class, an instance of which prints an object
- view_object.py a script with one command-line argument, the name of the pkled object to print

### Conversion
- convert.py defines constants and a general function to convert from one unit to another

### Time and Date
- date_time.py  various functions

### Text-to-speech
- speak.py  defines functions to use espeak to vocalise text and to expand abbreviations

### Persistance
- persistant.py  defines a Persistant class
--   Switch  a class for a simple on/off switch
--   Number - a class for a value which can be incremented and decremented - used for controling rates and indexing
--   Option - a class which allows the selection of an option

### Configuration
- conf.py  - Config class loads a config file 

#### files
- config/config.txt   - each line is name=value

### GPS
- gps.py  defines a GPS class to receive NMEA sentences and save the current gps data every 1 second
- geo.py defines a LatLong class which contains distance and bearing functions and other conversion functions
- start_gps.py  script to create the gps object and start it monitoring 

#### objects
- gps  GPS instance 

### Compass

- Devantech_CMPS10.py   defines a CMPS10 class to interface to the CMPS10 chip
- compass.py  defines a Compass class that gathers magnetic bearing data and converts to a true bearing
- start_compass.py  script to create a Compass object called 'compass' and start it monitoring every 1 seconds

#### objects 
- compass Compass instance 
- compassoffset  Number updated by calibrate so that bearings are relative to the direction of the mount 

### Track
- track.py  a track class with a monitor function which collects GPS and compass data periodically and logs to a serial file
- start_position_logger.py script to create a logg object and  start logging
- make_kml.py  takes a route and a track and generates kml
- replay_track.py - simulates a past track

#### objects  
-    log_sw  Switch to control logging
-    log_rate  Number to determine the rate of logging  in seconds

#### files  
-  log/{name}.txt   the log called name
-   kml/{name}.kml - generated kml from track name

### Route
- route.py  defines  Route and Waypoint classes
- start_route.py  starts the route object

#### objects 
-   route   Route object containg the current waypoints

### Data Talker
- start_talker.py  start up the talker

#### objects  
-  talk_sw     Switch to turn the talker on and off
-   talk_rate   Number to control the rate of talking - seconds
-  talk_mode   Option to determine what data is talked

#### files 
- routes/{name}.txt  set of waypoints as "|"  delimited data: name, latitude,longitude,datetime,description

### Library
- books.py  Book and Library(Persistant) class
- start_book_reader.py  starts a reader process 

#### objects
-  read_sw   Switch to turn reader on or off
-  library   Library which contains books and the current position in each book

#### files
-  texts{name}.txt book text - one line per voiced phrase

### Menu
- presenter.py class Presenter interprets presenter keypresses as cursor movements
- menu.py  class Menu describes a hierarchical menu and its actions
- xmlutils.py  support functions to modify the Menu XML code
- start_menu.py  start up a menu - parameter is a menu name

#### files 
-  menu/{name}.xml  a menu

### Start Up
- start.sh   - get the separate processes running

- ~/.profile  - edited to run start.sh on boot after auto login to pi


## To install
- copy all scripts to a directory
- run post_install.sh


