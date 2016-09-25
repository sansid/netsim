#!/usr/bin/python 
import sys

#file = open('sept19-temp-001.dat')
filename = sys.argv[1]
file = open(filename)
ts=[]
data=[]
for line in file:
    fields = line.strip().split()
    ts.append(fields[0])
    data.append(fields[1])
    #print fields[0], fields[1]

data_sent =0
print len(ts) 
i=0
step_size=1.0
time=0.0
b=0

while(i<len(ts)):
  time=float(ts[i])
  data_sent=0
  while(float(ts[i]) < step_size):
     if((i+1)>len(ts)):
        break
     else:
        data_sent+=int(data[i])
        i=i+1 
  print step_size ,data_sent*8
  step_size=step_size+1
  if ((i+1)>len(ts)):
     break
   
