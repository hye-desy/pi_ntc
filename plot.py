#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from datetime import datetime
from argparse import ArgumentParser
import math
import os
from glob import glob

#### get latest '.dat' file
list_of_files = glob('./*dat') 
latestfile = max(list_of_files, key=os.path.getctime)

#### argument
parser = ArgumentParser(description='Plot.')
parser.add_argument('-f', dest='datafile', default=latestfile)
args = parser.parse_args()

print(args.datafile)

#### initialization 
gpio=[17]

datelist=[[] for _ in range(len(gpio)*8)]
vallist=[[] for _ in range(len(gpio)*8)]

#### plot legends 
labellist=[]
for i in range(0,len(gpio)*8):
    labellist.append('gpio'+str(gpio[int(math.floor(i/8))])+'_'+str(i%8))

#### fill data into lists
with open(args.datafile,'r') as f:
    for line in f:
        a=line.split()
        for i in range(len(gpio)):
            if int(a[1])==gpio[i]:
                for j in range(0,8):
                    if int(a[2])==j:
                        vallist[i*8+j].append(float(a[3]))
                        datelist[i*8+j].append(datetime.strptime(a[0], "%a_%b_%d_%H:%M:%S_%Y"))

#### ploting
for i in range(0,len(gpio)*8):
    plt.plot_date(mdate.date2num(datelist[i]), vallist[i], '-', label=labellist[i])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.subplots_adjust(right=0.75)
plt.xlabel("Time")
plt.ylabel("T ($^\circ$C)")
plt.show()
