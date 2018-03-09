## Bits Calc ##
## Author: Abueesp ##
## Date: Tue, May 23 2015 ##
## License: CC NC-BY-SA ##

scriptname = 'Bits Calc'
prompt = '> '

print "Hello, I'm the", scriptname, "a pretty dumb code for calculating bits"

print "Introduce the number of bits: "
bits = int(raw_input(prompt))
bytes= bits/8
print "You have", bits, "bits, which are", bytes, "words of 8-bits also known as bytes."
print "\n"

print "Which represent the following bit positions"
if (bits % 2 == 0):
  for i in range(bits/2):
	  print 1,
elif(bits % 2 == 1):
  for i in range((bits-1)/2):
	  print 1,
  print 0
else:
  print 'Was that a number?'
print "\n"

possibilities=2**bits
dualities=possibilities/2
print "Which represent", possibilities, "possibilities, or", dualities, "dualities." 
print "\n"
