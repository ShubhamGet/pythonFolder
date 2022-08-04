class Demo:
    def clacy(self,a=None, b=None, c=None):
        add=0
        mul=0
        if(a!=None and b!=None and c!=None):
            add=a+b+c
            return add
        elif(a!=None and b!=None):
            mul=a*b
            return mul
        else:
            print("Nothing")

obj=Demo()
print(obj.clacy(2,3,4))
print(obj.clacy(2,3))
print(obj.clacy())
