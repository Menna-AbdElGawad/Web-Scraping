class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self) :
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound) :
        return f"{self.name} says {sound}"
    

dog = Dog("Buddy", 5)
print(dog.description())
print(dog.speak("Woof"))

dog = Dog("Bella", 4)
print(dog.species)