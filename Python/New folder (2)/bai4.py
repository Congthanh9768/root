x =  int (input("nhập vào một số: "))
uoc =  list()

for i in range (1,x):
    if(x % i == 0):
        uoc.append(i)
print("Các ước của %s là: " %x)
print(uoc)
