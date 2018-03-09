## Generalization of Collatz Conjecture ##
## Series: Number Theory ##
## Author: Abueesp ##
## Date: Mon, Nov 11 2017 ##
## License: CC NC-BY-SA ##

scriptname = 'Generalization of Collatz Conjecture'
prompt = '> '

print ("Hello, I'm the %scriptname, a pretty dumb code for easy testing of numbers according to any specific model of the Collatz Conjecture." % (scriptname))

print ("Introduce a number to test: ")
num = int(raw_input(prompt))
initialnum = num
print ("Introduce the coefficent for ax+b: ")
coefficent = int(raw_input(prompt))
print ("Introduce the constant for ax+b: ")
constant = int(raw_input(prompt))
counter = 0
while num > 1:
    if (num % 2) == 0:
        num = num / 2
	print ("Step %02d, Result %02d") % (counter, num)
	counter += 1
	print ("The number %01d takes %01d steps on n/2, until we get one 1.") % (initialnum, counter, coefficent, constant)
    else:
        num = num*coefficent + constant
	print ("Step %02d, Result %02d") % (counter, num)
    	counter += 1
	print ("The number %01d takes %01dx+%01d, until we get one 1.") % (initialnum, counter, coefficent, constant)
