n = int(input("nhap n : "))
sn = 1/(2*n)
for i in range(1,n):
    sn += 1/(2*i)
print("total : ",sn)
