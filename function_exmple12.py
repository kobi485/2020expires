from random import randint
def fun_list(x):
    for i in range(20):
        x.append (randint(1,100))

list1=[]
fun_list(list1)
print(list1)




def fun2(list1,y):
     x=list1.count(y)
     return x

y=int(input('enter number:'))
fun2(list1,y)
print(fun2(list1,y))

print(max(list1))

print(list1.index(max(list1)))