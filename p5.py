# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

maxNum = 20
num = maxNum
notFound = True
# primeArray = [7,8,9]
primeArray = [11,12,13,14,15,16,17,18,19]
primeArray = primeArray[::-1]

while notFound:

	num += maxNum

	for i in primeArray:
		if num % i == 0:
			notFound = False
		else:
			notFound = True
			break

	# print(num)

print(f"Ans: {num}")