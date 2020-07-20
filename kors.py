class kors:
    def __init__(self,number,name,stu,maxstu):
        self.number=number
        self.name=name
        self.stu=stu
        self.maxstu=maxstu

    def kobi(self):
            return (f'in the kors{self.nume}number{self.name}there is{self.stu}from max flaces of{self.maxstu}')


    def x (self):
            return ('the num of empty seating',{self.maxstu-self.stu})

kors1=kors(16,'idf',15,25)
print(kors1.x())
print(kors1.kobi())

