class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

class Dog(Animal):
    def __init__(self, name, breed):
        # super().__init__(name)  # Calling parent class __init__ method
        self.name = name
        self.breed = breed

    def speak(self):
        parent_speak = super().speak()  # Calling parent class speak method
        return f"{parent_speak} Woof!"

# Object
dog = Dog("Rex", "Labrador")
print(dog.speak())
