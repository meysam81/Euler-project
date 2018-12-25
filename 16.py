from math import *
n = 2 ** 1000
sum = 0
nStr = str(n)
for i in nStr:
	sum += int(i)
print(sum)