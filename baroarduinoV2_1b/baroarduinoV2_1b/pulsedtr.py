import serial
import time
import sys

#if len(sys.argv)!=2:
 #   print "port please"
  #  sys.exit(-1)

ser=serial.Serial('/dev/ttyACM0',57600,timeout=0)
ser.setDTR(1)
time.sleep(.5)
ser.setDTR(0)
ser.close()
