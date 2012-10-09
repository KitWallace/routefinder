from Adafruit_I2C import Adafruit_I2C

# ===========================================================================
# CMPS10 Class
# The CMPS10 board is developed by devantech 
# Chris Wallace 2012-09-19
# 2012-09-24  addresses corrected, magnetc and true bearings, @property
# ===========================================================================

class CMPS10(object) :
  __CMPS10_bearing8 = 0x01
  __CMPS10_bearing16 = 0x02
  __CMPS10_pitch = 0x04
  __CMPS10_roll = 0x05
  __CMPS10_X = 0x0A
  __CMPS10_Y = 0x0C
  __CMPS10_Z = 0x0E
  __CMPS10_dX = 0x10
  __CMPS10_dY = 0x12
  __CMPS10_dZ = 0x14
 
  def __init__(self, address=0x60,  debug=False):
    self.i2c = Adafruit_I2C(address)
    self.address = address
    self.debug = debug
 
  @property
  def magnetic_bearing(self):
    "Reads the high resolution compass bearing"
    bearing16 = float(self.i2c.readU16(self.__CMPS10_bearing16)) / 10
    if (self.debug):
      print "DBG: magnetic bearing: ", bearing16
    return bearing16 

  @property
  def pitch(self) :
    "Reads the pitch as a signed 8 bit angle in degrees"
    pitch = self.i2c.readS8(self.__CMPS10_pitch)
    if (self.debug):
      print "DBG: pitch: ", pitch
    return pitch

  @property
  def roll(self) :
    "Reads the roll as a signed 8 bit angle in degrees"
    roll = self.i2c.readS8(self.__CMPS10_roll)
    if (self.debug):
      print "DBG: roll: ", roll
    return roll

  @property
  def XYZ(self) :
    "Reads the raw XYZ magnatron values "
    XYZ = (self.i2c.readS16(self.__CMPS10_X),self.i2c.readS16(self.__CMPS10_Y),self.i2c.readS16(self.__CMPS10_Z))
    if (self.debug):
      print "DBG: raw: ", XYZ
    return XYZ

  @property
  def dXYZ(self) :
    "Reads the XYZ accelerometer values "
    dXYZ = (self.i2c.readS16(self.__CMPS10_dX),self.i2c.readS16(self.__CMPS10_dY),self.i2c.readS16(self.__CMPS10_dZ))
    if (self.debug):
      print "DBG: accelerometer: ", dXYZ
    return dXYZ

   
  def update(self) :   
    s = serial.Serial(port,4800)
    while True:
       nmea = s.readline()
       if nmea.startswith("$GPRMC") :
         self.update_with_RMC(nmea)
         self.put()
       elif nmea.startswith("$GPGGA") :
         self.update_with_GGA(nmea)

