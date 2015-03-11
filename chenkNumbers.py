# -*- coding: utf-8 -*-
# kratos0517


def checkNum(num1, num2):
	primes = []

	for i in range(num1, num2):
		count = i / 2
		while  count > 1:
			if i % count == 0:
				print "largest factor of %d is %d" %(i, count)
				break
			count -= 1
		else:
			if i != 0 and i != 1:
				primes.append(i)


	for j in primes:
		print j,