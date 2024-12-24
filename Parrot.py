class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying.")

    def sing(self):
        print(f"{self.name} is singing.")

class Parrot(Bird):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def talk(self):
        print(f"{self.name}, the {self.color} parrot, is talking!")

    def mimic(self, sound):
        print(f"{self.name} mimics: {sound}")

bird = Bird("Generic Bird")
bird.fly()
bird.sing()

parrot = Parrot("Polly", "green")
parrot.fly()
parrot.sing()
parrot.talk()
parrot.mimic("Hello!")
