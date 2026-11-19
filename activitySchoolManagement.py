# Parent Class
class Person:

  def __init__(self, name, age):
    self.name = name
    self.__age = age  

  def get_age(self):
    return self.__age

  def display_info(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.get_age()}")


# Child Class inheriting from Person
class Student(Person):

  def study(self):
    print(f"{self.name} is studying")


student1 = Student("Lina", 20)

student1.display_info()
student1.study()
