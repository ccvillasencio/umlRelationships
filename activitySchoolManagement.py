class Person:

  def __init__(self, name, age):
    self.name = name
    self.__age = age  

  def get_age(self):
    return self.__age

  def display_info(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.get_age()}")


person1 = Person("Lina", 20)

person1.display_info()

# Reflection: Why is it better to access __age through get_age()?
# Using get_age() protects the data from accidental changes outside the class.
# It also lets us control how the age is viewed or add validation rules later.
