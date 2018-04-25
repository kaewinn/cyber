#!/usr/bin/env python2
import sys
import re
import os

a = 4 #keep track if missing arguments

#byte or bit
if sys.argv[1] == '-B':
    setByte = True
    setBit = False
elif sys.argv[1] == '-b':
    setBit = True
    setByte = False
    interval = 1
else:
    print >> sys.stderr, "Byte or bit must be specified using -B for byte or -b for bit"

#retreive or store
if sys.argv[2] == '-s':
    setStore = True
    setRetrieve = False
elif sys.argv[2] == '-r':
    setRetrieve = True
    setStore = False
else:
    print >> sys.stderr, "Store or Retrieve must be specified using -s for store or -r for retreive"

#offset value (specified location in the wrapper)
if sys.argv[3].startswith('-o', 0, 2): 
    offset = sys.argv[3]
    offset = offset[2:]
else:
    print >> sys.stderr, "Offset must be specified using -o<val>"

#interval value (constant distance between each byte/bit of the hidden file in the wrapper)
if sys.argv[4].startswith('-i', 0, 2): 
    interval = sys.argv[4]
    interval = interval[2:]
    a=a+1
elif sys.argv[1] == '-B':
    print >> sys.stderr, "If in Byte, interval must be specified using -i<val>"

#set wrapper file
if sys.argv[a].startswith('-w', 0, 2):
    wfilename = sys.argv[a]
    wfilename = wfilename[2:]
    #wrapperfile = open(wfilename, mode = 'r', buffering = -1) #change buffering later
else:
    print >> sys.stderr, "Wrapper file must be specified using -w<val>"
a=a+1

#set hidden file
if setStore is True:
    if sys.argv[a].startswith('-h', 0, 2):
        hfilename = sys.argv[a]
        hfilename = hfilename[2:]
        #hiddenfile = open(hfilename, mode = 'r', buffering = -1) #change buffering later
    else:
        print >> sys.stderr, "Hidden file must be specified using -h<val>"

'''
if setByte is True and setBit is False:
    if setStore is True and setRetrieve is False:
        #
    elif setRetrieve is True and setStore is False:
        #
    else:
        print >> sys.stderr, ""
elif setBit is True and setByte is False:
    if setStore is True and setRetrieve is False:
        #
    elif setRetrieve is True and setStore is False:
        #
    else:
        print >> sys.stderr, ""
'''
#sentinel value = end of file
