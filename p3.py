# What is the largest prime factor of the number 600851475143 ?

import math

num = 600851475143
# num = 143
primeFactors = []

def findNextPrime(number):

	# print(number)
	# print(primeFactors)

	if number == 2:
		primeFactors.append(number)
		print("last added 2")
		return

	if number % 2 == 0:
		primeFactors.append(2)
		findNextPrime(number / 2)
		return

	primeArray = [2]

	for i in range(3, int(number+1)):

		newPrime = False

		for j in primeArray:

			# print(f"{i}, {j}, {number}, {primeArray}")

			if i == j:
				print("same")

			if i % j == 0:
				newPrime = False
				break
			newPrime = True
		
		if newPrime and i not in primeArray:
			primeArray.append(i)
			# print(f"Arr = {primeArray}")

		if number % i == 0:
			primeFactors.append(i)
			findNextPrime(number / i)
			break

findNextPrime(num)

print(f"Ans: {primeFactors}")