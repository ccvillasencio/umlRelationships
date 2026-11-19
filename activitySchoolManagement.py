class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display_info(self):
    print(f"Name: {self.name}")
    print(f"Age:{self.age}")


# Instantiate the object person1
person1 = Person("Lina", 20)

# Display the information
person1.display_info()
