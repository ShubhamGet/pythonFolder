# function overloading
"""
def add(datatype, *args):
    if datatype == 'int':
        answer = 0

    if datatype == 'str':
        answer = ''

    for x in args:
        answer = answer + x
    print(answer)

add('int', 5, 6)
add('str', 'Hi ', 'Shubham')
"""

# function overriding
class Base:
    def myfun(self):
        print("Base class Function ")

class Derived(Base):
    def myfun(self):
        print("Derived class Function ")

obj=Derived()
obj.myfun()


