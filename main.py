#class Car:
    #speed=110
    #def __init__(self,speed):
        #self.speed=speed_car
    #def info(self):
        #print("Швидкіть авто: ",self.speed)
#sp=int(input('Максимальна швидкість авто: '))
#auto=Car()
#print("Швидкіть авто: ",self.speed)
#auto.info()
#auto2=Car(180)
#auto2.info()

#class Pupils:
    #def __init__(self,name,height):
        #self.name=name
        #self.height=height
    #def __str__(self):
        #print("Ім'я учасника: ",self.name, "Зріст учасника: ",self.height)

#p1=Pupils("Ігор",height: 155)
#p1.__str__()
#p2=Pupils("Оля",height: 158)
#p2.__str__()
#p3=Pupils("Петро",height: 162)
#p3.__str__()
#print(p1.count,"учасника змагань")

#Симулятор студента
import random as r
class Student:
    def __init__(self,name):
        self.name=name
        self.happy=r.randint(a=10,b=100)
        self.progress=r.randint(a=0,b=10)
        self.alive=True
        self.money=r.randint(a=0,b=200)

    def study(self):
        print('Час для навчання')
        self.happy-=r.randint(a=1,b=50)
        self.progress+=r.randint(a=1,b=5)

    def chill(self):
        print('Відпочинок')
        self.happy+=r.randint(a=1, b=50)
        self.progress-=r.randint(a=1, b=5)
        self.money-=r.randint(a=1, b=50)

    def sleep(self):
        print('Сон')
        self.happy+=r.randint(a=1, b=50)
        self.progress-=r.randint(a=1, b=5)

    def money(self):
        print('Робота')
        self.happy+=r.randint(a=1, b=50)
        self.progress-=r.randint(a=1, b=5)

    def isAlive(self):
        if 0<self.progress<5:
            print('Ти на грані відрахування.')
            self.progress+=r.randint(a=1,b=10)
        elif self.progress<1:
            print('Ти відрахований.')
            self.alive=False
    def everyday(self):
        print("Рівень щастя", self.happy)
        print("Прогрес навчання", self.progress)
        print(str(self.money)+' грошей')
        if self.money<=30:
            print('Ти повинен йти на роботу.')
            self.money+=r.randint(a=30, b=100)
    def studyLife(self,day):
        day="Місяць №"+str(day)
        print(day)
        res=r.randint(a=1,b=4)
        if res==1:
            self.study()
        elif res==2:
            self.chill()
        elif res==3:
            self.sleep()
        elif res==4:
            self.study()
        res = r.randint(a=1, b=4)
        if res == 1:
            self.study()
        elif res == 2:
            self.chill()
        elif res == 3:
            self.sleep()
        elif res == 4:
            self.study()
        self.everyday()
        self.isAlive()

st1=Student('Олег')
print("Життя студента", st1.name)
for k in range(1,13):
    if st1.alive==False:
        break
    st1.studyLife(k)