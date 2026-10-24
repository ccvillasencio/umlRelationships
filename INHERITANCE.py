class Animal:
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"


# --- Running the code ---
my_dog = Dog("Buddy")

print(my_dog.bark())
