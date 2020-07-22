def func(str):
    str1=''
    for i in str:
        if i!='a':
            str1+=i
    return str1


str='aabgfdadf'
print(func(str))
