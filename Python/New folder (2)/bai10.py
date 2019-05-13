import random
print("1. Rock")
print("2. Secissor")
print("3. Paper")
dic = {"Rock" : 1 ,"Secissor": 2, "Paper": 3}
user = int(input("Bạn chọn: "))
computer = random.randint(1,3)
if(user == 1):
    if(computer == 2):
        print("Bạn thắng")
    elif(computer == 3):
        print("bạn đã thua")
    else:
        print("Hòa")
elif(user == 2 ):
    if(computer == 3):
        print("Bạn thắng")
    elif(computer == 1):
        print("Ban đã thua")
    else:
        print("Hòa")
else:
    if(computer == 1):
        print("Bạn thắng")
    elif(computer == 2):
        print("Bạn đã thua")
    else:
        print("Hòa")


                 
