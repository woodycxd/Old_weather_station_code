#! /usr/bin/python
import serial
import time
import datetime
import logging
import subprocess
import collections
test=10
forever=1
buffer=' '
moving_ave=collections.deque('0000000000')
moving_ave_index=0
moving_ave_flag=0
ser=serial.Serial('/dev/ttyACM0',57600)
ser.setDTR(1)
time.sleep(.5)
ser.setDTR(0)
time.sleep(2)
logging.basicConfig(filename='logger.csv',level=logging.DEBUG)
while forever==1:
        #output=open("logger.csv","a")
      try:
        print"here loop 1"
        while test>0:
            try:
               buffer=ser.read(ser.inWaiting())
            except:
               call("ssmtp woodycxd@gmail.com < /home/pi/baroarduinoV2_1b/baroarduinoV2_1b/msg.txt",shell=True)
	    if '\n' in buffer:
		data=buffer	
                split_data=data.split(",",6)
                print(str(split_data[4]))
                now=datetime.datetime.now()
                moving_ave.popleft()
                moving_ave.append(str(split_data[4]))
                ave_temp=(float(moving_ave[0])+float(moving_ave[1])+float(moving_ave[2])+float(moving_ave[3])+float(moving_ave[4])+float(moving_ave[5])+float(moving_ave[6])+float(moving_ave[7])+float(moving_ave[8])+float(moving_ave[9]))/10
                print moving_ave
                print str(ave_temp)
                logging.debug(","+str(data).rstrip('\n\r')+","+str(ave_temp)+","+str(now.year)+","+str(now.month)+","+str(now.day)+","+str(now.hour)+","+str(now.minute)+","+str(now.second)+"\r")
                print(str(data).rstrip('\n\r')+","+str(ave_temp)+","+str(now.year)+","+str(now.month)+","+str(now.day)+","+str(now.hour)+","+str(now.minute)+","+str(now.second))
                if mov_ave_flag==1:
                   buffer=' '
	    time.sleep(1)
            test=test-1
      except Exception: 
         pass

        #output.close()
        #time.sleep(1)
      test=10
        #time.sleep(1)


