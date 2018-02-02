def zoj(n):
	if(n % 2 == 0):
		return True
	else:
		return False

n1 = 1
n2 = 2
sum = 0
while(n1 < 4*10**6):
	if(zoj(n1)):
		sum = sum + n1
	n3 = n1 + n2
	n1 = n2
	n2 = n3
		
print (sum)
	