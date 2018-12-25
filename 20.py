def fact (n):
	s = n
	for i in range (2, n):
		s *= i
	return s
def add (n):
	s = 0
	for i in n:
		s += int (i)
	return s
print (add(str(fact(100))))