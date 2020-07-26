class bus:
    def __init__(self,sits):
        self.sits=sits
        self.list1=[]
        for i in range(self.sits):
            self.list1.append('free')


    def geton(self,name):
        for i in range(len(self.list1)):
            if self.list1[i]=='free':
                self.list1[i]=name
                break
        else:
            print(f'the bus is full,(name) not go up ')

    def __str__(self):
        return f'sits:{self.sits} number off pussenger:{bus1.list1}'







bus1=bus(20)
x=(bus1.list1)
print(bus1.list1)

(bus1.geton('kobi'))
bus1.geton('avi')
bus1.geton('kodi')
print(bus1)
