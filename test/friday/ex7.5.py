from random import randint
dic1={}

for a in range(10):
    dic1[a]=randint(1,100)

print(dic1)

sum=0
for i in dic1.values():
    sum+=i
print(sum)


sum2=0
for i in dic1:
    sum2+=dic1[i]
print(sum2)
