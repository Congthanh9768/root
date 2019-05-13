import random
def newlist(list_a):
    return(list_a[0],list_a[len(list_a) - 1])
a = random.sample(range(1,100), 12)
b = newlist(a)
print(a)
print(b)
