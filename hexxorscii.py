#!/usr/bin/env python

#This program can be used to XOR hex values with another hex value, and then convert it from hex to ascii.

hexList = []

while True:
	hexValue = raw_input("Enter a two byte hex value (format ex: 5A) or press ENTER to finish: ")
	if hexValue == '':
		break
	else:	
		hexList.append(hexValue)

print "\n"	
print "====================================="	
print "You entered the following hex values:"
print(hexList)
print "====================================="
print "\n"

xorValue = input("Enter the hex value you wish to use for the XOR function (format ex: 0x7): ") 

result = (list(['{:02x}'.format( int(i, 16) ^ xorValue) for i in hexList]))

print "\n"
print "[+]XORing list and converting from hex to ascii..."
print "[+]Result:"
print bytearray.fromhex(''.join(result)) 
