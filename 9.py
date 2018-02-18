def pythagoreanTriplet(a, b, c):
	t = False
	if ((a**2 == b**2 + c**2) or \
		(a**2 + b**2 == c**2) or \
		(a**2 + c**2 == b**2)):
			t = True;
	return t
for i in range(1, 1000):
	for j in range(1, 1000):
		if(i + j < 1000):
			for k in range(1, 1000):
				if(i + j + k == 1000):
					if(pythagoreanTriplet(i, j, k)):
						print (i * j * k)
						break