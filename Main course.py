from package1.Course import Course
from package1.Student import Student

course1=Course(5,'qa',20)
course1.subjects={'unit test':'michal tal','python':'orly Q','shit':'8200'}

id=int(input('enter number:'))
while id>0:
    name=input('enter name:')
    stud=Student(id,name)
    for subject in course1.subjects.keys():
        stud.grades[subject]=int(input('enter number:'))
    course1.add_student(stud)

