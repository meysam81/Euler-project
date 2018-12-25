def divisor (n):
	mList = []
	for i in range (1, int (n ** 0.5) + 1):
		if (n % i == 0):
			mList.append(i)
			test = int (n / i)
			if (test != i):
				mList.append(test)
	#mList
	#mList = sorted(mList)
	mList.sort()
	del (mList[-1])
	return mList
def add (n):
	sum = 0
	for i in n:
		sum += i
	return (sum)
s = 0
for i in range (2, 10001): # i = 220
	xList = divisor(i)
	x = add(xList) # x = 284
	if (x != i):
		yList = divisor(x)
		y = add(yList)
		if (y == i):
			s += x
print(s)

