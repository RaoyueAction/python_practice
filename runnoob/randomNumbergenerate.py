import random
a = random.random()
b = random.randint(0,10)
list1 = [1,2,3,4,5]
list2 = ['a','b','c']
c = random.choice(list1)
d = random.choices(list1)
e = random.shuffle(list1)

print(a,b,c,d)

print(list1)