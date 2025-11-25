#aynı arayüzün farklı davranmasına olanak tanır
#koda esniklik ve genişletibilirlik kazandırırız


"""
class Animal:
    def make_sound(self):
        print("The animal makes a sound")
class Dog(Animal):
    def make_sound(self):
        print("The dog barkss")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows")
animals = [Dog(),Cat()]
for animal in animals:
    animal.make_sound()


class Bird:
    def make_sound(self):
        print("Bird Chirps")
class Dock:
    def make_sound(self):
        print("Duck quakcs")

def animal_sound(animal):
    animal.make_sound()

bird = Bird()
dick = Dock()

animal_sound(bird)
animal_sound(dick)
"""

class Animal:
    def make_sound(self):
        print("Some generic animal sound")
class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")
class Dog(Animal):
    def make_sound(self):
        print("Hav Hav")
class Cow(Animal):
    def make_sound(self):
        print("Moo Moo")

class Duck(Animal):
    def make_sound(self):
        print("Quack Quack")

###simulator clas

class AnimalSoundSimulator:
    def __init__(self):
        self.animals =[]
    def add_animal(self,animal):
        if isinstance(animal,Animal):
            self.animals.append(animal)
            print(f"{animal.__class__.__name__} addet to the simulator")
        else:
            print("Invalid animal type")

    def make_all_sound(self):
        if not self.animals:
            print("No animals in the simulator")
        else:
            print("Hayvan sesleri")
            for animal in self.animals:
                animal.make_sound()

simulator = AnimalSoundSimulator()
while True:
    print("1. Add Dog")
    print("2. Add Cat")
    print("3 Add Cow")
    print("4. Add Duck")
    print("5 Make All Sounds")
    print("6. Exit")
    choice = input("Enter your choice(1-6)")
    if choice == "1":
        simulator.add_animal(Dog())
    elif choice == "2":
        simulator.add_animal(Cat())

    elif choice == "3":
        simulator.add_animal(Cow())
    elif choice == "4":
        simulator.add_animal(Duck())
    elif choice == "5":
        simulator.make_all_sound()
    elif choice == "6":
        print("Exiting the simulator GoodBye")
        break
    else:
        print("Invalid Choice Plase Try Again")
