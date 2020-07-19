from random import randint

l=int(input('enter low number:'))
u=int(input('enter upper number:'))
k=int(input('enter num of number:'))
list1=[]
for i in range(k):
    num=randint(l,u)
    list1.append(num)
print(list1)


set1=set()
for i in range(k):
    num=randint(l,u)
    set1.add(num)
print(set1)

