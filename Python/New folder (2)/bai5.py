import  random
a = [1 , 1 , 2 , 3 , 5 , 8 , 13 , 21, 34 , 55 , 89]
b = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13]
dic = dict()
for i in a:
   if i in b:
       dic[i] = i
ls = list()
for k ,v in dic.items():
    ls.append(k)
print(ls)
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30) , 16)
result = [i for i in set(a) if i in b]
print(a)
print(b)
print(result)

