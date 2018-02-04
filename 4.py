def isPalindrome(n):
	hold = n
	result = 0
	while(n > 0):
		#print("result = ", result, ", hold = ", hold, ", n = ",n)
		result = (result * 10) + (n % 10)
		n = int(n / 10)
	#print("result = ", result, ", hold = ", hold, ", n = ",n)
	if(result == hold):
		return True
	else:
		return False
def test(n1, n2):
	max = 1
	for i in range(n2, n2 - 100, -1):
		for j in range(n2, n2 - 100, -1):
			if(isPalindrome(i * j)):
				if(max < (i * j)):
					max = i * j
	return max
print(test(99,999))