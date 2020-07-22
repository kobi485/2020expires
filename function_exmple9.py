def f2(x):
    if 0<x<19:
        return 'child'
    elif 18<x<61:
        return "adult"
    elif 60<x<121:
        return 'senior'
    else:
        return 'error'


for i in range(5):
    x=int(input('enter number:'))
    print(f2(x))