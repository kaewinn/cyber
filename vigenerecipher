# Kaelyn Nguyen
# CSC 442-001
# Program 2: Vigenere Cipher: encrypts or decrypts messages
# Python 3: "python3 p2.py -e mykey"

import sys
    
def readFile():
    if sys.stdin.isatty() == False: #isatty() returns false if there's something in stdin
        #there is a file
        text = sys.stdin.read() # read file
    else:
        # there is no file
        text = None
    return text

def cipher(a, k, minus):
    a = list(a) #split characters of intext
    k = list(k) #split characters of key

    anum = [] #number equivalents of alpha characters for intext
    knum = [] #number equivalents of key characters
    
    #turn characters into integers for the INTEXT
    for i in range(len(a)):
        if a[i].isalpha() == True: #if it's a character in the alphabet // numbers and symbols are not
            if a[i].islower() == True: #if it is lowercase
                anum.append(alpha.index(a[i])) #add the number equivalent of the alpha letter
            else: #it's uppercase
                anum.append(ALPHA.index(a[i])) #add the number equivalent of the alpha letter
        else:
            anum.append(a[i]) #add the number or symbol, (no number equivalent) 

    #turn characters into integers for the KEY
    for i in range(len(k)):
        if k[i].isalpha() == True:
            knum.append(alpha.index(k[i]))

    b = [] #outtext 

    j = 0    
    for i in range(len(anum)):
        if type(anum[i]) == int: #if it is an integer
            if minus == "-e": #encrypt
                num = (anum[i] + ((knum[j%len(knum)])))%26
                j+=1
            elif minus == "-d": #decrypt
                num = (26 + anum[i] - (knum[j%len(knum)]))%26
                j+=1
                
            letter = alpha[num] #output letter
        else: #for numbers and symbols
            letter = anum[i]       
        
        b.append(letter) #add the output letter into the outtext

    #check if original intext charcter was uppercase
    #if yes: force outtext character to be uppercase    
    for i in range(len(a)):
        if a[i].isupper() == True:
            b[i] = b[i].upper()

    outtext = ''.join(b) #join together all single characters into a single string
    
    return outtext


################## main
args = list(sys.argv) #list of arguments
minus = args[1] #-e or -d is 2nd argument passed in
key = args[2].lower() #key is the 3rd argument passed in

#lowercase and uppercase ignored
#same letter has same integer representation
global alpha
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
global ALPHA
ALPHA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

file = readFile()
if file != None: #if there was a file passed in
    intext = file
    outtext = cipher(intext, key, minus)
    print(outtext)

# if we are decrpyting AND a file was passed in, we do not wait for input after decryption
if not ((minus == "-d") and (file != None)): 
    while True: 
        try:
            intext = input() #wait for input
            outtext = cipher(intext, key, minus)
            print(outtext)
        except(EOFError): #catch CTRL+D and exit nicely
            break



