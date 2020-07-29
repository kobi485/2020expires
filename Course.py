from package1.Student import Student

class Course:
    def __init__(self,num,name,maxstu):
        self.num=num
        self.name=name
        self.subjects={}
        self.students=[]
        self.maxstu=maxstu

    def __str__(self):
            return (f'this is course:{self.name}number:{self.num} our subject is:{self.subject} and our student:{self.student} we have a max numbers of student:{self.maxstu} ')

    def add_student(self,student):
        if len(self.students)<self.maxstu:
            self.students.append(student)
            return True
        else:
            return False

    def add_factor(self,subject,factor):
        for Student in self.students:
            Student.calc_factor(subject,factor)

    def del_student(self,id):
        for student in self.students:
            if student.id==id:
                self.students.remove(student)
                break



    def calc_avg(self):
        sum=0
        for student in self.students:
            sum+=student.avarge()
        sum=sum/len(self.students)
        return sum



