class Animal:
    def __init__(self,name):
        self.name=name
        self.ung=5
        self.energy=5

    def __str__(self):
        return (f'the animal is {self.name} ung={self.ung} energy= {self.energy}')

    def eat(self,food):
        self.ung-=food/50
        self.energy-=food/100
        if self.ung<0:
            self.ung=0
            print ('the animal is full and didnt finish eat')
        if self.energy<0:
            self.energy=0

    def play(self,time):
        self.energy-=(time/10)*2
        self.ung+=(time/10)*2
        if self.energy<0:
            self.energy=0
            print('the animal is tried')
        if self.ung>10:
            self.ung=10

    def rest(self,chill):
        self.energy+=chill/20
        self.ung+=chill/30
        if self.energy>10:
            self.energy=10
            print('animal finish rest and she wanted play')
        if self.ung>10:
            self.ung=10
            print('animal finish rest give him food')




animal1 = Animal('dog')
num=int(input('enter number 0-3:'))
while num!=0:
    if num==1:
        animal1.eat(int(input('how much gram?')))
        print(animal1)
    if num==2:
        animal1.play(int(input('how much time?')))
        print(animal1)
    if num==3:
        animal1.rest(int(input('how much time?')))
        print(animal1)
    num = int(input('enter number 0-4:'))
print(animal1)












# print(animal1)
# animal1.eat(100)
# print(animal1)
# animal1.play(20)
# print(animal1)
# animal1.rest(300)
# print(animal1)





