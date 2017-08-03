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
import sys, re
from barron import Barron

# Range selector string to list
def parse_range(range_str):
    ''' Range Selector parsing, from selector string to a list

    A Range selector is used to select a range of integers. For example,
    [1,2,3,6,7,9,10,11] can be written as "1-3,6,7,9-11". Comma is used
    to seperate them, and the numbers does not need to be in order. To parse
    the above selector, use:
        parse_range('1-3,6,7,9-11')
    which returns a sorted list of integers.
    '''

    # Seperate the values by comma, and strip white spaces
    elements = [a.strip() for a in range_str.split(',')]
    normal = re.compile('^(\d+)$')
    special = re.compile('^(\d+)-(\d+)$')

    # Use set to prevent repetitive storage
    selection = set()

    for e in elements:
        # Single Integer match
        m = normal.match(e)
        if m:
            selection.add(int(m.group(1)))
            continue

        # Range Integer Match
        m = special.match(e)
        if m:
            start = int(m.group(1))
            end = int(m.group(2))
            if end < start:
                raise ValueError('Error Parsing range %s: End < Start' % e)
            for i in range(start, end + 1):
                selection.add(i)
    return sorted(selection)


# List to simplified range selector string
def revparse_range(selection_list, prefer_dash = False):
    ''' Range Selector parsing, from integer list to simplist range selector.
    Pass [1,2,3,6,7,9,10,11] to the function yields the result "1-3,6,7,9-11".

    If perfer_dash is set to true then the function yields "1-3,6-7,9-11".
    '''
    # Sort the list first, then initialize counters
    selection_list.sort()
    results, start, end = [], 0, 0

    while end < len(selection_list):
        end += 1
        # If index reached the end or not continuous
        if end >= len(selection_list) or selection_list[end - 1] + 1 != selection_list[end]:
            results.append(str(selection_list[start]))

            # Prefer dash and no perfer dash mode
            if prefer_dash:
                if end - start > 1:
                    results[-1] += '-%d' % selection_list[end - 1]
            else:
                if end - start > 2:
                    results[-1] += '-%d' % selection_list[end - 1]
                elif end - start > 1:
                    results.append(str(selection_list[end - 1]))

            start = end

    return ','.join(results)

if __name__ == '_main__':
    # Parse the arguments
    R = sys.argv[1]  # take in parameter about range
    try:
        C = int(sys.argv[2])
    except IndexError:
        C = 100

    # open resources
    sav = open('barron_testpaper.txt','w')	# this file will be saved

    barron = Barron('res', 'txt')
    bundles = barron.list_bundles()
    for i, n in enumerate(bundles):
        print('[%d] %s' % (i, n))

    user_selection = int(input('Enter Selection (0) ==> ') or 0)
    word_list = bundles[user_selection]

    
    selection = parse_range(R)
    words = barron.load_words(word_list,selection)

    # Randomly select number of words
    selected_words = random.sample(words.keys(), C)

    list_info = '# %s List %s' % (word_list, revparse_range(selection))

    # Write to file and print to console
    print('\n' + list_info + '\n')
    sav.write(list_info + '\n\n')

    for i, w in enumerate(selected_words):
        word_line = '%03d   %s' % (i + 1, w)
        print(word_line)
        sav.write(word_line + '\n')

    sav.close()

    print('\n%s has been successfully written to \'barron_testpaper.txt\'.' % list_info)
