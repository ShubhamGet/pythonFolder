"""
class Faculty:

   def __init__(self, faculty):
      self.name = faculty['name']
      self.subject = faculty['subject']

   def get_faculty_details(self):
      return f"Name: {self.name}\nSubject: {self.subject}"
"""

class Faculty:
   def __int__(self, faculty, name, subject):
      self.name=name
      self.subject=subject

   def get_faculty_details(self):
      print("Name ",self.name,"Subject ",self.subject)

