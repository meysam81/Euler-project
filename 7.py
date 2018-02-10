import calendar
import time
def isPrime(n):
	t = True
	for i in range(2 , int(n**0.5) + 1, 1):
		if(n % i == 0):
			t = False
			break
	return t
#print(int(18**(0.5)))
count = 9
start = calendar.timegm(time.gmtime())
for i in range(29, 1000000000):
	if(isPrime(i)):
		count = count + 1
	#print("i = ", i, ", count = ", count)
	if(count == 10001):
		print(i)
		break
end = calendar.timegm(time.gmtime())
print(end - start)
#2 3 5 7 11 13 17 19 23 29