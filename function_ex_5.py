def fun(num):
    sum=0
    for i in range(num):
        sum+=(i)+1
    return sum
for i in range(5):
    num = int(input('enter number:'))
    print(fun(num))


