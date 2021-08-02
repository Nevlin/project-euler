# Find the largest palindrome made from the product of two 3-digit numbers.

maxN = 998001
ans = 0
products = [0,0]

def palindromeCheck(num):
	convert = str(num)
	if convert == convert[::-1]:
		return True
	else :
		return False

for i in range(100, 1000):
	for j in range(100, 1000):
		total = i * j
		if palindromeCheck(total) and total > ans:
			ans = total
			products = [i, j]

print(f"Answer = {ans}")
print(products)