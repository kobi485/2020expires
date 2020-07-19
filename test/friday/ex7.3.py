dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
list1=list(dic1.values())
lis2=list(dic1.keys())
dic2={}
for i in range (len(lis2)):
    dic2[list1[i]]=lis2[i]
print(dic2)
print(list1)
print(lis2)