#from math import *
numStrYekan = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numStr10to19 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
numStrDahgan = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
numStrSadgan = 'hundred'
numStrHezargan = 'thousand'
numStrAnd = 'and'
sum = 0
#n = 121
for i in range(1, 1001):
	#print(i)
	num = ""
	if(i == 1000):
		num += numStrYekan[1] + numStrHezargan
	elif((i <= 999) and (i >= 100)):
		#print(numStrSadgan[int(i % 100 / 10)])
		#print(floor((i % 100)))
		num += numStrYekan[int(i / 100)] + numStrSadgan
		tempStr2Digit = (i % 100)
		if(tempStr2Digit >= 10) and (tempStr2Digit <= 19):
			num += numStrAnd + numStr10to19[tempStr2Digit % 10]
		elif(tempStr2Digit <= 9) and (tempStr2Digit >= 1):
			num += numStrAnd + numStrYekan[tempStr2Digit % 10]
		elif(tempStr2Digit >= 20):
			num += numStrAnd + numStrDahgan[int(tempStr2Digit / 10)] + numStrYekan[int(tempStr2Digit % 10)]
	else:
		tempStr2Digit = i % 100
		if(tempStr2Digit >= 10) and (tempStr2Digit <= 19):
			num += numStr10to19[tempStr2Digit % 10]
		elif(tempStr2Digit <= 9) and (tempStr2Digit >= 1):
			num += numStrYekan[tempStr2Digit % 10]
		elif(tempStr2Digit >= 20):
			num += numStrDahgan[int(tempStr2Digit / 10)] + numStrYekan[int(tempStr2Digit % 10)]
	sum += len(num)
	#print(num)
print(sum)