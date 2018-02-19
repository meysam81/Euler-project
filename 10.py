def isPrime(n):
	t = True
	for i in range(2, int(n**(0.5)) + 1):
		if(n % i == 0):
			t = False
			break
	return t
sum = 0
for i in range(2, 2*10**6):
	if(isPrime(i)):
		sum = sum + i
print(sum)