#!/usr/bin/env python
## -*- coding: utf-8 -*-

# barron_testpaper_generator.py
  
# Copyright 2017 Hisen Zhang <hisenzhang@gmail.com>
  
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
  
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
  
  

from random import randint 
import sys

# load argv

R = int(sys.argv[1])  # take in parameter about range
if len(sys.argv) == 3: # if the number of words are given
	C = int(sys.argv[2])
else:					# default # of words = 100
	C = 100

# initializing lists (containers)
wordlist,buff = [],[]	
f    = [file]*10
text = ['']*R

# open resources
sav  = open('barron_testpaper.txt','w')	# this file will be saved
f[0] = open('./rsc/barron_01-05.hisen')	# resourses
f[1] = open('./rsc/barron_06-10.hisen')
f[2] = open('./rsc/barron_11-15.hisen')
f[3] = open('./rsc/barron_16-20.hisen')
f[4] = open('./rsc/barron_21-25.hisen')
f[5] = open('./rsc/barron_26-30.hisen')
f[6] = open('./rsc/barron_31-35.hisen')
f[7] = open('./rsc/barron_36-40.hisen')
f[8] = open('./rsc/barron_41-45.hisen')
f[9] = open('./rsc/barron_46-50.hisen')
	
#load recourses into RAM according to range R given
for i in range(0,R):
	text[i] = f[i].read()

# reshape
for i in text:
	wordlist = wordlist + i.split(' ')

# combine and send to print buff
for i in wordlist:
	buff.append(i)

# list info
list_info = '# Barron List 1-'+str(5*R)+' #\n\n'
print '\n'+list_info
sav.write(list_info)

# kernel
counter = 1
for i in buff:
	while counter <= C:
		i = randint(0,len(buff)-1)
		print str(counter).zfill(3)+'   '+buff[i]
		sav.write(str(counter).zfill(3)+'   '+buff[i]+'\n')
		counter += 1

# close all files	
for i in f:
	i.close()
sav.close()
print '\n# Barron List 1-'+str(5*R)+' ('+str(C)+' words) has been successfully written to \'barron_testpaper.txt.\'\n'

