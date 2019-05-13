def isPrime2(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


#ans = 0
for i in range(1, 40):
    if isPrime2(i):
         print(i)
    #    ans = i
    #if i % 10000000 == 0:
     #   print(i)
#print(ans)
