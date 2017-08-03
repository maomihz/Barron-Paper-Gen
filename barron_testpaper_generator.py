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



import random
import sys, os, re
from barron import Barron


SAVE_FILE = 'barron_testpaper.txt'
WORD_LIST = 'dummy'

def parse_range(range_str):
    elements = [a.strip() for a in range_str.split(',')]
    normal = re.compile('^(\d+)$')
    special = re.compile('^(\d+)-(\d+)$')

    selection = set()

    for e in elements:
        # Single number match
        m = normal.match(e)
        if m:
            selection.add(int(m.group(1)))
            continue
        m = special.match(e)

        # Range Number Match
        if m:
            start = int(m.group(1))
            end = int(m.group(2))
            if end < start:
                raise ValueError('Error Parsing range %s: End < Start' % e)
            for i in range(start, end + 1):
                selection.add(i)
    return sorted(selection)

def revparse_range(selection_list):
    if len(selection_list) == 0:
        return ''
    if len(selection_list) == 1:
        return str(selection_list[0])


    selection_list.sort()
    results = []
    start = 0
    end = 0
    while end < len(selection_list):
        while end < len(selection_list) - 1 and selection_list[end] + 1 == selection_list[end + 1]:
            end += 1

        if end - start > 1:
            results.append('%d-%d' % (selection_list[start], selection_list[end]))
        else:
            results.append('%d' % selection_list[end])

        start = end + 1
        end = start
    return ','.join(results)


# Parse the arguments
R = sys.argv[1]  # take in parameter about range
try:
    C = int(sys.argv[2])
except IndexError:
    C = 100

# open resources
sav = open(SAVE_FILE,'w')	# this file will be saved

barron = Barron('res', 'txt')
bundles = barron.list_bundles()
for i, n in enumerate(bundles):
    print('[%d] %s' % (i, n))

user_in = int(input('Enter Selection ==> '))
WORD_LIST = bundles[user_in]


selection = parse_range(R)
words = barron.load_words(WORD_LIST,selection)

# Randomly select number of words
selected_words = random.sample(words.keys(), C)

list_info = '# %s List %s' % (WORD_LIST, revparse_range(selection))

# Write to file and print to console
print('\n' + list_info + '\n')
sav.write(list_info + '\n\n')

for i, w in enumerate(selected_words):
    word_line = '%03d   %s' % (i + 1, w)
    print(word_line)
    sav.write(word_line + '\n')

sav.close()

print('\n%s has been successfully written to \'barron_testpaper.txt\'.' % list_info)
