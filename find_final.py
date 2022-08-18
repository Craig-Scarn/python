#!/usr/bin/python3
import os
import re
cmd = 'ls -l'
pattern = '[Pp][Aa@]..[Ww][Oo0][Rr][Dd]*'

#Get list of files
output = os.popen(cmd).read()
line = output.rstrip()
line = output.split()
#print(line)

files = []
for i in line:
    if 'txt' in i:
        files.append(i)

#print(files)
line2 = '' 
for item in files:
    hand = open(item)
    for line in hand:
        line = line.rstrip()
        if re.findall(pattern, line):
            print(item, '---', line)




'''
for line in hand:
    line = line.rstrip()
    if re.findall(pattern, line):
        print(line)'''