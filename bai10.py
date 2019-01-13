print("chương trình tìm giá tri khi ta mod còn dư 1")
n = int(input("nhap n: "))
mod = int(input("nhap mod: "))
for i in range(-10, 300):
    if(n*i - (int((n*i)/mod))*mod == 1):
        print(i)
