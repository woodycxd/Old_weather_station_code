#! /usr/bin/python
import time
import datetime
import csv
import shutil
import pdb
import pycurl
import pytz
shutil.copy2('/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/logger.csv','/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/loggercopy.csv')
time.sleep(.5)
infile=open('/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/loggercopy.csv','r')
outfile=open('/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/lastline.txt','w')
new_outfile=open('/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/nl.txt','w')
barooutfile=open('/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/baroline.txt','w')
lightoutfile=open('/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/lightline.txt','w')
comboOutfile=open('/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/combo.txt','w')
comboOutfile2=open('/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/combo2.txt','w')
comboOutfile3=open('/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/combo3.txt','w')
ave_temp_out_file=open('/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/ave_temp.txt','w')
www_outfile=open('/home/pi/baroarduinoV2_1b/baroarduinoV2_1b/www_out.txt.txt','a')
time.sleep(.5)
mytz=pytz.timezone('US/Eastern')
#data=csv.reader(infile,delimiter=",")
#for debug,pressure,value,temp,space,ave_temp,year,month,day,hour,mint,sec in data:
for line in infile:
    last =line
print(str(last)) # last complete form
line=str(last)     
spline=line.split(',',1) #split line on "," results in 2 items debug callout and data
print spline
print spline[1]
spline[1]=spline[1].rstrip('\r\n')  #strip return and line feed from data string
spline=spline[1].split(',',12) #split data string into 11 seperate items
print"here"
print "6="+spline[6]
print "5="+spline[5]
print "4="+spline[4]
print "3="+spline[3]
print "2="+spline[2] # temperature  value
print "1="+spline[1] # light value
print "0="+ spline[0] # baro value
value=spline[1]
raw_pressure=int(spline[0]) 
pressure=raw_pressure*.00498
pressure=(((pressure/5.1)+.095)/.009)
pressure=pressure*.2953
temp=float(spline[4])
new_temp=float(spline[3])
ftemp=temp*-.189296927+174.0563177676 #was 175.
f_new_temp=6.00*new_temp#5.371  5.82
f_new_temp=(f_new_temp-500.00)/10.0
f_new_temp=(9/5)*f_new_temp+32
print new_temp
print f_new_temp
ave_temp=float(spline[6])
ave_temp=ave_temp*-.189296927+174.0563177676
#pdb.set_trace()

print str(ftemp)
mydate=datetime.datetime.utcnow()
mydatestring=mydate.strftime('%H')
utcday=mydate.strftime('%d')
#pdb.set_trace()
c=pycurl.Curl()
c.setopt(c.URL,'http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php')
c.setopt(c.POSTFIELDS,'ID=KVTSHAFT2&PASSWORD=icomr8500&dateutc='+str(spline[7])+'-'+str(spline[8])+'-'+utcday+'+'+mydatestring+'%3A'+str(spline[11])+'%3A'+str(spline[12])+'&tempf='+str(ave_temp)+'&baromin='+str(pressure)+'&action=updateraw')
c.perform()
www_outfile.write(str(spline[7])+'-'+str(spline[8])+'-'+utcday+'+'+mydatestring+'%3A'+str(spline[11])+'%3A'+str(spline[12])+'&tempf='+str(ave_temp)+'&baromin='+str(pressure)+'\n\r')
#outfile.write(str(ftemp)+', '+str(spline[4])+', '+str(spline[5])+', '+str(spline[6])+', '+str(spline[7])+', '+str(spline[8]))
outfile.write(str(spline[5])+'-'+str(spline[6])+'-'+str(spline[7])+'T'+str(spline[8])+':'+str(spline[9])+':'+str(spline[10])+'-5:00'+','+str(ftemp))
barooutfile.write(str(spline[5])+'-'+str(spline[6])+'-'+str(spline[7])+'T'+str(spline[8])+':'+str(spline[9])+':'+str(spline[10])+'-5:00'+','+str(pressure))
#new_outfile.write(str(spline[5])+'-'+str(spline[6])+'-'+str(spline[7])+'T'+str(spline[8])+':'+str(spline[9])+':'+str(spline[10])+'-5:00'+','+str(f_new_temp))
new_outfile.write('0'+','+str(f_new_temp))
if(int(value)>50):
        iradvalue=(float(int(value)*2))*1E-6
        iradvalue=1/iradvalue
        #tempstring=str(value)+','+str(iradvalue)+","+str(day)+","+str(hour)+","+","+str(mint)+"\n"
        lightoutfile.write(str(spline[4])+'-'+str(spline[5])+'-'+str(spline[6])+'T'+str(spline[7])+':'+str(spline[8])+':'+str(spline[9])+'-5:00'+','+str(iradvalue))
elif(int(value)<50):
        lightoutfile.write(str(spline[4])+'-'+str(spline[5])+'-'+str(spline[6])+'T'+str(spline[7])+':'+str(spline[8])+':'+str(spline[9])+'-5:00'+','+str(value))

comboOutfile.write('0'+','+str(ftemp)+'\n\r')
comboOutfile2.write('1'+','+str(pressure)+'\n\r')
ave_temp_out_file.write('0'+','+str(ave_temp)+'\n\r')
#comboOutfile3.write('2'+','+str(iradvalue)+'\n\r')
#pdb.set_trace()

infile.close()
outfile.close()
new_outfile.close()
barooutfile.close()                 
lightoutfile.close()
comboOutfile.close()
comboOutfile2.close()
comboOutfile3.close()
ave_temp_out_file.close()
www_outfile.close()

