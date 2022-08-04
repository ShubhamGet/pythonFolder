class Students:
    def getData(self):
        self.__ename=input("Enter name ")
        self.__eid=int(input("Enter id "))
        self.__age=int(input("Enter age "))

    def show(self):
        print("Student name is ",self.__ename)
        print("Student eid is ",self.__eid)
        print("Student age is ",self.__age)

class Marks(Students):
    def getMarks(self):
        self.__m1=int(input("Enter marks 1 "))
        self.__m2=int(input("Enter marks 2 "))
        self.__m3=int(input("Enter marks 3 "))
    
    def showdata(self):
        print("Marks1 ",self.__m1)
        print("Marks2 ",self.__m2)
        print("Marks3 ",self.__m3)

obj=Marks()
obj.getData()
obj.getMarks()
obj.show()
obj.showdata()