## Collatz Conjecture ##
## Series: Number Theory ##
## Author: Abueesp ##
## Date: Mon, Nov 11 2017 ##
## License: CC NC-BY-SA ##

scriptname = 'Collatz Conjecture'
prompt = '> '

print ("Hello, I'm the %scriptname, a pretty dumb code for easy testing of numbers according to the Collatz Conjecture." % (scriptname))

print ("Introduce a number: ")
num = int(raw_input(prompt))
initialnum = num
counter = 0

while num > 1:
    if (num % 2) == 0:
        num = num / 2
	print ("Step %02d, Result %02d") % (counter, num)
	counter += 1
    else:
        num = num*3 + 1
	print ("Step %02d, Result %02d") % (counter, num)
    	counter += 1

print ("The number %01d takes %01d steps till get one 1.") % (initialnum, counter)
