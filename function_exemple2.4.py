def fun(num):
    y=2
    if num % y == 0:
        while y <= num:
            y = y + 1
        return ('not prime')
    else:
        return ('prime')


x=int(input('enter number:'))
print(fun(x))