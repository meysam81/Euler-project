myFile = open("p022_names.txt", "r")
alph = [i for i in "abcdefghijklmnopqrstuvwxyz"]



myList = myFile.read().lower().split(",")
#myList = myList[0:10]
myList.sort()
for i, x in enumerate(myList):
	myList[i] = x[1:-1]
#print(myList)
#myList = ["COLIN".lower()]
sum = 0
for index, i in enumerate(myList):
	elSum = 0
	for j in i:
		#val = next((i + 1 for i, x in enumerate(alph) if x == j), None)
		#val = 0
		for ind, x in enumerate(alph):
			if x == j:
				#print (j, x, ind + 1)
				elSum += (ind + 1)
	elSum *= (index + 1)
	sum += elSum
	#print (index + 1, ":", i, elSum, "\nsum is:", sum, "\n=============================")
	#print(index + 1, i, elSum, sum)
	#print("==========================")
	
print(sum)