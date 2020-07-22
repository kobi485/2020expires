def fun1(x):
    list1=[]
    for i in range (x):
        i=int(input('enter number:'))
        list1.append(i)
    return list1

def fun2(list):
    return sum(list)/len(list)



x=int(input('enter number of student:'))
list3=(fun1(x))
print(fun2(list3))


