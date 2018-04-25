# Kaelyn Nguyen
# CSC 442-001
# Program 1: Binary Decoder: reads binary encoded message 7 or 8 bit ASCII
# Python 3 "$ python3 p1.py < binary1.txt"

import sys

#read in file inputs
def read():
    binary = sys.stdin.read()
    b = list(binary) #splits the string into single characters 
    b.remove("\n") #\n is unnecessary so we remove it
    return b

def decode():
    b = read()
    seven = []
    eight = []

    #group bits together
    i = 0
    j = 0
    while i < len(b):
        seven.append(''.join(b[i:i+7]))
        i += 7
    while j < len(b):
        eight.append(''.join(b[j:j+8]))
        j += 8

    #convert binary into decimal
    for i in range(len(seven)):
        seven[i] = int(seven[i], 2)
    for i in range(len(eight)):
        eight[i] = int(eight[i], 2)

    #convert decimal into ASCII equivalent
    bit = 7
    for i in range(len(seven)):
        seven[i] = chr(seven[i])
        char = seven[i]

        bs = False #backspace
        if char == '\b': #literal string of backspace
            bs = True
            
        if ((char.isprintable() == False) and (bs == False)): #if not printable, whitespace, or bs
            bit = 8
            break
        
        decode = seven
        
    if bit == 8:
        for i in range(len(eight)):
            eight[i] = chr(eight[i])
        decode = eight

    #join all single characters into a string
    d = ''.join(decode)
        
    return d


####### main
d = decode() 
print(d)


    
