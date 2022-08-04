from this import s


n=5
students=[]
for num in range(n):
    name=input("Enter the name of students ")
    students.append(num)

marks=[]
for num in range(n):
    marks=int(input("Enter the marks of students "))
    students.append(marks)

data=input("Do u wanna show the data ")

if data=='Yes':
    for i,j in zip(students,marks):
        print(i,':',j)