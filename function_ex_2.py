def x(num):
    if 99<num<1000:
        return True
    else:
        return False
num=int(input('enter number:'))
if x(num):
    print('true')
else:
    print('no')