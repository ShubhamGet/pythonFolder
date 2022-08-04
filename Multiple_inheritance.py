class Rectangel:
    def Get(self,height,widht):
        area=widht*height
        print("Area of Rectange",area)

class Squre:
    def value(self,squ):
        area=squ*squ
        print("Area of square ",area)

class Sum(Rectangel,Squre):
    def add(self,num1,num2):
        total=num1+num2
        print("Sum of two number ",total)

obj=Sum()
obj.Get(2,4)
obj.value(4)
obj.add(2,4)



