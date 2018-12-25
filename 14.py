def collatzProblem(n):
	#result = 0
	#print(n)
	#if(n == 1):
		#return n
	if(n % 2 == 0):
		return(int(n / 2))
	else:
		return(int(3 * n + 1))
	#return result
max = 0
hold = 0
result = 0
for n in range(2, 10**6):
	count = 0
	hold = n
	while(n != 1):
		#print(n)
		count = count + 1
		if(count > max):
			max = count
			result = hold
		n = collatzProblem(n)
print(result)