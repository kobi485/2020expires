class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.grades= {}

    def add_grade(self,subject,grade):
        self.grades[subject]=grade

    def __str__(self):
        return (f'i am student number{self.id} my name is {self.name} and my grades is{self.grades}')

    def calc_factor(self,subject,factor):
        self.grades[subject]=(self.grades[subject]*factor)/100+self.grades[subject]

    def avarge(self):
            sum=self.grades.values()/len(self.grades)
