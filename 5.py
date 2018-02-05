def isSmallest(n):
	t = True
	for i in range(1, 20):
		#print("i= ", i, ", n= ", n)
		if(n % i != 0):
			
			t = False
			break
	return t
for j in range(11, 100000000000):
	if(j % 2 == 0):
		if(isSmallest(j)):
			print(j)
			break