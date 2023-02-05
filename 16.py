class Animal:
    def __init__(self, legs_count):
        print("Animal object created")
        self._number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._number_of_legs} legs")

    def return_legs(self):
        return self._number_of_legs

class Dog(Animal):
    def __init__(self, name, legs_count):
        super().__init__(legs_count)
        self._name = name

    def bark(self):
        print("Woof wof")

dog = Dog("Max", 4)
dog.bark()
print(dog._name)
dog.count_legs()
print(dog.return_legs())
