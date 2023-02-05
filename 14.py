class Animal:
    def __init__(self, legs=4):
        self.legs = legs
        print("Animal object created")

    def run(self):
        print("Running started")

    def count_legs(self):
        print("Number of legs:", self.legs)

    def return_legs(self):
        return self.legs

animal = Animal()
animal.run()
animal.count_legs()
print("Number of legs (direct):", animal.legs)
print("Number of legs (returned):", animal.return_legs())
