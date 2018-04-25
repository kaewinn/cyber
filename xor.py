#!/usr/bin/env python2
import sys
import binascii

# This function takes 2 strings (an input and a string) and XORs them to get an output string
def xorBits(inputstring, keystring):
        
        # These two lines translate the inputstring and keystring into binary
        inputbin = bin(int(binascii.hexlify(inputstring), 16))
        keybin = bin(int(binascii.hexlify(keystring), 16))
        
        # This stores the value of the XORed input and key bits
        outputbin = (int(inputbin, base = 2)^int(keybin, base = 2))
        
        # This translates the binary output into a string to be returned
        outputstring = binascii.unhexlify('%x' % outputbin)
	return outputstring

# This reads the input from standard input (a file)
inputstring = str(sys.stdin.read())

# These opens a changeable file called 'key' in read mode, and then reads its contents
keyfile = open('key', mode='r', buffering=-1)
keystring = keyfile.read()

# This calls the function to XOR the input and the key
outputstring = xorBits(inputstring, keystring)

# This prints the output to standard output (either the terminal or a file, whichever is specified)
print outputstring

# This closes the key file
keyfile.close()
