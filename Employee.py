class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Display(self):
        print("My name is:", self.name)
        print("My id is:", self.id)

class worker(Person):
    def __init__(self, name, id, salary):
        super().__init__(name, id) 
        self.salary = salary

obj = worker("Bob", 578346, 100000)
obj.Display()
