## Mersenne Primes Code ##
## Series: Arithmetic Primes ##
## Author: Abueesp ##
## Date: Tue, May 23 2015 ##
## License: CC NC-BY-SA ##

scriptname = 'Woodall Prime Code'
prompt = '> '

print "Hello, I'm the %scriptname, a pretty dumb code for easy testing of Woodall primes (n*2^n-1)." % (scriptname)

print "Introduce a prime number (remember, 1 and 0 are not prime numbers): "
prime = int(raw_input(prompt))

print "How many iterations do you want to calculate?:"
iterations = int(raw_input(prompt))
for i in range(iterations):
	prime=prime*(2**prime)-1
	print prime
exit()
