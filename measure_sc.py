#!/usr/bin/python

import time
import RPi.GPIO as GPIO
from MCP3008 import MCP3008
from NTC10kOhm import NTC10kOhm

filenamehead=""
#filenamehead="ntc10kOhm"

sleeptime=2


if __name__ == "__main__":

    if filenamehead!="":
	of_dat=open(filenamehead+"_"+time.ctime().replace(" ","_").replace("__","_").replace(":","-")+".dat","w")


    ntc=NTC10kOhm()
#    adcs=[MCP3008(bus=0, device=0)]
#    adcs=[MCP3008(bus=1, device=0),MCP3008(bus=1, device=1), MCP3008(bus=1, device=2)]
    adcs=[MCP3008(bus=0, device=0), MCP3008(bus=0, device=1)]

    try:
	while True:
	    print "\n-------------------------"
	    print time.ctime()

	    for idx, adc in enumerate(adcs):
		print 'sc',idx
		for channel in range(0,8):
#		    time.sleep(0.2)
#		    adc.open()
		    value = adc.read(channel)
#		    adc.close()

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
	for adc in adcs:
	    adc.close()
	print "keyboard interrupt"


