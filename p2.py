# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

sumTotal = 2
fibArray = [1,2]

while fibArray[1] < 4000000:
	fibArray.append(fibArray[0] + fibArray[1])
	if fibArray[2] % 2 == 0:
		sumTotal += fibArray[2]
	fibArray.pop(0)

print(sumTotal)