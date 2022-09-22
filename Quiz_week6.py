#10 questions about classes, objects, inheritance, polymorphism, queues, stacks, and more

#create a class called Queue. 
# The class should have the following methods: enqueue, dequeue, and size. 
# The enqueue method should add an item to the queue. 
# The dequeue method should remove an item from the queue. The size method should return the size of the queue.

#create a class called Stack. The class should have the following methods: push, pop, and size. 
# The push method should add an item to the stack. The pop method should remove an item from the stack. 
# The size method should return the size of the stack.




#1 ----
# #create a credit card class with the following attributes: card number, expiration date, and security code. 
# Create a method that will print out the card number, expiration date, and security code. 
# Create an instance of the class and call the method.


class Credit_Card:
    def __init__(self, card_number, expiration_date, security_code):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code
        
    def info(self):
        return f"Number: {self.card_number}\nExp Date: {self.expiration_date}\nSec Code: {self.security_code}"

card = Credit_Card("34567234", "30/12/2023", "12356")

card.info()

print(card.info())

# #2 ------
# # #create Animal class and Dog class. 
# # Make the Dog class inherit from the Animal class. 
# # Add a bark method to the Dog class. Create an instance of the Dog class and call the bark method.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        return f"{self.name} is barking"

dog = Dog("Police")
dog.bark()
print(dog.bark())

#3 -------
#create a class called Queue. 
# The class should have the following methods: enqueue, dequeue, and size. 
# The enqueue method should add an item to the queue. 
# The dequeue method should remove an item from the queue. The size method should return the size of the queue.

data = []



# #4 ------------
# #create a class called Person. 
# # The class should have the following attributes: name, age, and address. 
# # The class should have the following methods: eat, sleep, and work. 
# # The eat method should print out the name of the person and the word "is eating".
# #  The sleep method should print out the name of the person and the word "is sleeping". 
# # The work method should print out the name of the person and the word "is working".

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age  = age
        self.address = address
        
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def work(self):
        print(f"{self.name} is working")


p = Person("Patrick", 31, "Bukaya")

p.eat()
p.sleep()
p.work()
    
# #5 
# # Create a subclass of Employee called Programmer. 
# # The Programmer class should have the following attributes: name, age, salary, and programming language. 
# # The Programmer class should have the following methods: eat, sleep, work, and code. 
# # The code method should print out the name of the person and the word "is coding in" and the programming language. 
# # Create an instance of the Programmer class and call all the methods.

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age  = age
        self.salary = salary
        
    def eat(self):
        pass

    def sleep(self):
        pass

    def work(self):
        pass

    def code(self):
        print(f"{self.name} is coding in Python")

e = Employee("Patrick", 31, 700000)
e.eat()
e.work()
e.code()


# #6----------
# #create a class called Vehicle. The class should have the following attributes: make, model, and year. 
# # The class should have the following methods: start, stop, and drive. 
# # The start method should print out the make, model, and year of the vehicle and the word "is starting". 
# # The stop method should print out the make, model, and year of the vehicle and the word "is stopping". 
# # The drive method should print out the make, model, and year of the vehicle and the word "is driving". 
# # Create a subclass of Vehicle called Car. 
# # The Car class should have the following attributes: make, model, year, and color. 
# # The Car class should have the following methods: start, stop, drive, and park. 
# # The park method should print out the make, model, year, and color of the car and the word "is parking". 
# # Create an instance of the Car class and call all the methods.


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year  = year
    

    def start(self):
        print(f"{self.make},{self.model}, {self.year} is starting")

    def stop(self):
        print(f"{self.make},{self.model}, {self.year} is stopping")

    def drive(self):
        print(f"{self.make},{self.model}, {self.year} is driving")

    
class Car(Vehicle):
    def __init__(self, make, model, year, color):
        self.color = color
        super().__init__(make, model, year)

    def start(self):
        return super().start()
        
    def stop(self):
        return super().stop()
        
    def drive(self):
        return super().drive()
    

    # make, model, year, and color of the car and the word "is parking".
    def park(self):
        print(f"{self.make}, {self.model}, {self.year}, {self.color} is parking")


car = Car("Mercedes", "A-class", 2022, "brown")
car.start()
car.stop()
car.drive()
car.park()


#7 
#create a class called Animal. The class should have the following attributes: name, color, and age. 
# The class should have the following methods: eat, sleep, and make_sound. 
# The eat method should print out the name of the animal and the word "is eating". 
# The sleep method should print out the name of the animal and the word "is sleeping". 
# The make_sound method should print out the name of the animal and the word "is making a sound". 
# Create a subclass of Animal called Dog. The Dog class should have the following attributes: name, color, age, and breed. 
# The Dog class should have the following methods: eat, sleep, make_sound, and bark.
# The bark method should print out the name of the dog and the word "is barking". 
# Create an instance of the Dog class and call all the methods.


class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age  = age
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def make_sound(self):
        print(f"{self.name} is making a sound")

class Dog(Animal):
    def __init__(self, name, color, age, breed):
        self.breed = breed
        super().__init__(name, color, age)

    def eat(self):
        return super().eat()

    def sleep(self):
        return super().sleep()
        
    def make_sound(self):
        return super().make_sound()

    def bark(self): 
        print(f"{self.name} is barking")
    

dog = Dog("Popi", "Brown", 3, "German")

dog.eat()
dog.sleep()
dog.make_sound()
dog.bark()

# 8
#create a class of your choice. It should have at least 3 attributes and 
# 3 methods where one of the methods is a static method.
# Implement polymorphism, encapsulation, and inheritance.

class User:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.__salary  = 700000 

    def login():
        pass
   # def :
        pass
    
class Student(User):
    def __init__(self, name, age, id_number, grade):
        self.grade = grade
        super().__init__(name, age, id_number)

    def attend_class(self):
        return f"Please attend class Regularly"


class teacher(User):
    def __init__(self, name, age, id_number, lesson_taught):
        self.lesson_taught = lesson_taught
        super().__init__(name, age, id_number)


    def get_salary(self):
        return hours

    set get_salary(self):