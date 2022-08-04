"""
class Student:

   def __init__(self, student):
      self.name = student['name']
      self.gender = student['gender']
      self.year = student['year']

   def get_student_details(self):
      return f"Name: {self.name}\nGender: {self.gender}\nYear: {self.year}"
"""
class Student:
   def __int__(self,student,name,age,gender):
      self.name=name
      self.age=age
      self.gender=gender

   def get_student_details(self):
      print("Name ",self.name,"Age ",self.age,"Gender ",self.age)
