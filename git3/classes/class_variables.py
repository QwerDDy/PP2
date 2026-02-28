class Person:
    species = "Human"
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Bob")

Person.species = "Alien"  

print(p1.species)  
print(p2.species)  


class Per:
    def __init__(self, name):
        self.name = name  

p1 = Per("Alice")
p2 = Per("Bob")

p1.name = "Carol"

print(p1.name) 
print(p2.name) 