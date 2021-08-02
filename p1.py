# Find the sum of all the multiples of 3 or 5 below 1000

sumThree = 0
sumFive = 0
maxNum = 1000

loopTotal = 0
i = 0
while loopTotal < maxNum:
	sumThree += loopTotal
	# sumThree.append(loopTotal)

	i += 1
	loopTotal = 3 * i


loopTotal = 0
i = 0
while loopTotal < maxNum:

	if loopTotal % 3:
		sumFive += loopTotal
		# sumFive.append(loopTotal)

	i += 1
	loopTotal = 5 * i

print(f"3: {sumThree}")
print(f"5: {sumFive}")
print(sumThree + sumFive)