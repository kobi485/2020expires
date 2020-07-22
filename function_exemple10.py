def f2(x):
    if 69<x<101:
        return True
    elif 0<x<70:
        return False

for i in range(5):
    x=int(input('enter number:'))
    if f2(x):
        print('test')
    else:
        print('fail')
        