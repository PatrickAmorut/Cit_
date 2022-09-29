#1
#Your task is to create slightly different animals, which should have the same properties and methods, 
# but should implement the talk() method in different ways. For example. 
# should a cat (when talking) say "Moew", a dog "Woff", a fish "Blub" and a Cow "Muuu". 
# They should all share the following (private) properties: name (string), age (number), food (list of strings), 
# and have the functions get_name, set_name, get_age, set_age, get_food, add_food, remove_food. 
# Finally, all the animals must have the talk function, but that function must, as I said, be 
# implemented in each animal, as the animals have different sounds.
# When you have made the classes, create instances of the classes and put in a list - loop through the list - 
# and let all the animals talk! :)

class Animal():
    def __init__(self, name, age, food):
    
        
        self.__name = ""
        self.__age = int
        self.__food = []

    def add_food(self, meal):
        self.meal = meal
        self.food.append(meal)
        return f"{self.__name} eats {self.meal}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name


    def get_age(self, age):
        return self.__age

    def set_age(self, age):
        self.__age = age
        return self.__age

    def get_food(self):
        return Animal.add_food()
    
    def remove_food(self):
        return f"Food has been removed"


    def talk(self, sound):
       return 0

class Dog(Animal): 
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
    
    def talk(self, sound):
        self.sound = sound
        return f"{self.name} make {self.sound}" 
        
class Cat(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def talk(self, sound):
        self.sound = sound
        return f"{self.name} make {self.sound}" 

class Cow(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def talk(self, sound):
        self.sound = sound
        return f"{self.name} make {self.sound}" 

a = Dog("jakie", 23, ["meat", "chicken"])

print(a.set_name("Popi"))
print(a.set_age(3))



# 2 The snail climbs up 7 feet each day and slips back 2 feet each night.
#  How many days will it take the snail to get out of a well with the given depth?. 
# Using python, write a function to solve this problem. Sample Input: 31 Sample Output: 6

# day = 7
# night = 5
# actual distance climbed is 5 feet




#3 Write a function that takes a list of numbers and returns the largest number in the list.


a = [1,2,3,4,6,7,99,88,999]
max_num = 0
for i in a:
    if i > max_num:
        max_num = i
print(max_num)

#4 Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
# Suppose the following input is 
# supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

def calc(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( f"No. of Upper case characters : {u}\nNo. of Lower case characters : {l}")

calc("Hello world!")


#7 Write a Program in Python to implement 
# a Stack Data Structure using Class and Objects, with push, pop, and traversal methods.


class Stack:
    def __init__(self):
        self.stack = list()

    
    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if self.isEmpty():
            return f"stack is empty. "
        
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack

s = Stack()
s.push(2)
s.push(4)
s.push(12)
print(s.show())
print(s.peek())
print(s.pop())

#9 Using only functions and lists, Implement a queue data structure. The queue should have the following 
#methods: enqueue, dequeue, and size. The queue should be "first-in-first-out" (FIFO)


list_1 = list()
maximum = 5

def isEmpty():
    return len(list_1) == 0 



def isFull():
    return len(list_1) == maximum

def enqueue(element):
    if not isFull():
        list_1.insert(0,element)
        return list_1
    else:
        return 'list is already full'


def dequeue():
    if not isEmpty():
        list_1.pop()
        return list_1

    else:
        return 'yo the list is already empty'

def display(f):
    print(f)

display(enqueue(6))
display(enqueue(7))
display(enqueue(8))
display(enqueue(9))
display(enqueue(10))
display(isFull())
display(enqueue(1))