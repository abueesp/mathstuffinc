## Mersenne Primes Code ##
## Series: Arithmetic Primes ##
## Author: Abueesp ##
## Date: Tue, May 23 2015 ##
## License: CC NC-BY-SA ##

scriptname = 'Mersenne Prime Code'
prompt = '> '

print "Hello, I'm the %s, a pretty dumb code for easy testing of Mersenne primes (2^n-1). Take into account that if n is prime then 2^n-1 is prime too." % (scriptname)

print "Introduce a prime number (remember, 1 and 0 are not prime numbers): "
prime = int(raw_input(prompt))

print "How many iterations do you want to calculate?:"
iterations = int(raw_input(prompt))
for i in range(iterations):
	prime=(2**prime)-1
	print prime
