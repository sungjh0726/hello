class dog:
    def __init__(self):
        self.name = ("dog")
        print("dog가 태어났어")
    
    def sing(self):
        print("랄라", self.name)

    def wag(self):
        print("dog's wag tail")

    def __del__(self)
        print("destroy")

puddle = Dog()


class Puppy(Dog):
    def __init__(self, name):
        self.name = name
        print("Puppy was Born")

    def wag(self):
        print("Puppy's wag tail")

puppy = Puppy('PP')
puppy.speak()
print("Name is", puppy.name)
print("isDog", isinstance(puppy, Dog))
puppy.test()

marry = Dog()