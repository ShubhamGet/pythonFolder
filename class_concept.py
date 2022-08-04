class Employee:
    def getData(self):
        data=[]
        for i in range(1,3):
            self.__eid=int(input("Enter the Id of Employees "))
            self.__ename=input("Enter the Name of Employees ")
            self.__eage=int(input("Enter the Age of Emplyees "))
            self.__esal=int(input("Enter the Salary of Employees "))
            data.append[self.__eid,self.__ename,self.__eage,self.__esal]

        print(data)
    
    def showData(self):
        for i in range(1,3):
            print("Employee ID is ",self.__eid)
            print("Employee Name is ",self.__ename)
            print("Employee Age is ",self.__eage)
            print("Employee Salary is ",self.__esal)
    

obj=Employee()
obj.getData()
obj.showData()
