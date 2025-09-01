class Animal:
    def __init__(self, name: str):
        self.name = name
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:        #override
        return f"{self.name} says: Woof!"


class Cat(Animal):
    def __init__(self, name: str, lives: int = 9):
        super().__init__(name) #Intialize Animal part
        self.lives = lives
    def speak(self) -> str:
        return f"{self.name} says: Meow!"


pets = [Dog("Fido"), Cat("Luna")]
for p in pets:
    print(p.speak())  #Polymorphism: Same call, different behavior