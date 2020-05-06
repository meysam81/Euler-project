def isPrime(n):
    for i in range(2 , int(n**0.5) + 1, 1):
        if(n % i == 0):
            return False
    return True


#2 3 5 7 11 13 17 19 23 29
count = 9
i = 29

while True:
    if(isPrime(i)):
        count = count + 1
    if(count == 10001):
        print(i)
        break
    i += 2
