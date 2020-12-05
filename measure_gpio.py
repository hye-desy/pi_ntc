#!/usr/bin/python

import time
import RPi.GPIO as GPIO
from MCP3008 import MCP3008
from NTC10kOhm import NTC10kOhm

gpio=[17,27,22]

#filenamehead=""
filenamehead="ntc10kOhm"

sleeptime=5



if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)

    for i in gpio:
	GPIO.setup(i, GPIO.OUT, initial=1)

    if filenamehead!="":
	of_dat=open(filenamehead+"_"+time.ctime().replace(" ","_").replace("__","_").replace(":","-")+".dat","w")


    ntc=NTC10kOhm()
    adc = MCP3008()

    try:
	while True:
	    print "\n-------------------------"
	    print time.ctime()

	    for i in gpio:
#	    time.sleep(1)
		print("gpio%d"%i)

		for channel in range(0,8):
		    
		    time.sleep(0.1)
		    GPIO.output(i,GPIO.LOW)
		    adc.open()
		    value = adc.read(channel)
		    adc.close()
		    GPIO.output(i,GPIO.HIGH)

		    V=ntc.VoltageCal(value)
		    R=ntc.ResisCal(value)
		    T=ntc.ThermistorCal(value)
		    if V>0.1 and V<3.2:
			print("channel%i, V: %.2f, R: %.2fk, T: %.2f"% (channel,V,R,T) )
#			print("channel%i, T: %.2f"% (channel,T) )
			if filenamehead!="":
			    of_dat.write(time.ctime().replace(" ","_").replace("__","_")+" "+str(i)+" "+str(channel)+" "+str("%.2f"%T)+"\n")


	    if sleeptime>0:
		time.sleep(sleeptime)

    except KeyboardInterrupt:
	if filenamehead!="":
	    of_dat.close()
	GPIO.cleanup()
	print "keyboard interrupt"


