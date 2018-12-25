def check(num):
	up = int(num ** 0.5) + 1
	sum = 1
	for i in range(2, up):
		if num % i == 0:
			sum += i
			if num / i != i:
				sum += (num / i)
	return sum > num
upBound = 28123 
# abundants = [False] * (upBound + 1)
abundants = []
for i in range(12, upBound):
	if check(i):
		# abundants[i] = True
		abundants.append(i)
canAbundants = [False] * (upBound + 1)
for i in abundants:
	for j in abundants:
		if i + j <= upBound:
			canAbundants[i + j] = True
		else:
			break
sum = 0
for i in range(upBound): 
	if canAbundants[i] == False:
		sum += i
print(sum)