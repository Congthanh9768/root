x = int(input("nhap vao mot so : "))
def giaithua(x):
    if(x==0):
        return 1
    else:
        return x * giaithua(x - 1)
print(giaithua(x))
