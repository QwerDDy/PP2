class Person:
    def greet(self):
        print("Hello from Person")

class Worker:
    def work(self):
        print("Working...")

class Employee(Person, Worker):  
    pass

e = Employee()
e.greet() 
e.work()   