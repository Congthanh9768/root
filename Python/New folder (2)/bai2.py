number  = int(input("input number: "))
if number % 2 == 0:
    print(number,"là so chăn")
else:
    print(number, " là số lẻ")
if(number %4==0):
    print(number , "là số chia hết cho 4")
else:
    print(str(number) +  " là số khong chia hết cho 4")
num = int(input("nham so chia het: "))
if number % num == 0:
    print(number, "Là số chia hết cho ",num)
else:
    print(number, "La số không chia hết cho ",num)
    
