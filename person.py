class person:
    def __init__(self,name,age,number):
        self.name=name
        self.age=age
        self.number=number


    def __str__(self):
        return (f'i am {self.name},i am {self.age},years old and i have,{self.number},children')

    def hasChildren(self):
        if int(self.number)>0:
            return (True)
        else:
            return (False)

    def ageGroup(self):
        if 19>int(self.age)>0:
            return ('child')
        elif 61>int(self.age)>18:
            return ('adult')
        elif 121>int(self.age)>60:
            return ('senior')
        else:
            return ('error')



person1=person('avi',21,'5')
print(person1)
if person1.hasChildren()==True:
    print('avi have children')
else:
    print('avi is lonely')
print(person1.ageGroup())

