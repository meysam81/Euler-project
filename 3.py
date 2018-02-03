import calendar
import time
def isPrime(n):
	t = True
	for i in range(2, int(n**(0.5))):
		if(n % i == 0):
			t = False
			break
	return t
n = 600851475143 
max = 2
start = calendar.timegm(time.gmtime())
for i in range(int(n**(0.5)), 2, -1):
	if(isPrime(i)):
		if(n % i == 0 and max < i):
			max = i
			break
end = calendar.timegm(time.gmtime())
print(end - start)
print(max, end = "")