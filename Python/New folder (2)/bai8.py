import random
a = random.randint(1,9)
chose = int(input("nhap vao mot so: "))
if (chose<a):
    print("so ban nhap vao nho hon so ngau nhien")
elif(chose > a):
    print("so ban nhap vao lon hon so ngau nhien")
else:
    print("so ban nhap vao bang so ngau nhien")
dem = 0
while True:
    str = input("nhap vao mot so de tiep tuc và khac nhap exit: ")
    if(str == "exit"):
        break
    else:
        chose = int(str)
        dem+=1
        if (chose<a):
            print("so ban nhap vao nho hon so ngau nhien")
        elif(chose > a):
            print("so ban nhap vao lon hon so ngau nhien")
        else:
            print("so ban nhap vao bang so ngau nhien")
    
print("so lan ban nhap vao la %s lan" %dem)
