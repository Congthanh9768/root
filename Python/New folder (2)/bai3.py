array = [1,4,2,5,7,9,2,3]
array.sort()
num1 = int(input("input num1: "))
print("day so nho hon ",num1)
for i in range(0,len(array)):
    if array[i] < num1:
        print("number %d "%array[i])
    else:
        break
a  = list()
for i in range(0,len(array)):
    if array[i] < num1:
        a.append(array[i])
    else:
        break
print(a)
b =  list()
number = int(input("input so muon in: "))
for i in range(0,number):
    if array[i] < num1:
        b.append(array[i])
    else:
        break
print(b)
print("áhfdjashkfdjahkjf")
print([i for i in array if(i < 5)])
