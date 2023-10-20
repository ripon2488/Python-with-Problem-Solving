''' Problem 1: Shape Area Calculation
Implement a class hierarchy using polymorphism '''

class Shape: #Base Class
    def calculate_area(self): # Base class Method
        pass

class Rectangle(Shape): #Inherit the base class
    def calculate_area(self,length,width): # Overridden base class method
        self.length=length
        self.width=width
        print(f"The Area of Rectangle is: ",self.length * self.width)

class Circle(Shape):
    def calculate_area(self,radius): # Overridden base class method
        self.radius=radius     
        print(f"The Area of Circle is: ",3.141 * (self.radius**2))

rectangle=Rectangle() # Calling Class in a object
rectangle.calculate_area(4,2) #  Calling overridden method for Rectangle()

circle=Circle() # Calling Class in a object
circle.calculate_area(4) #  Calling overridden method for Circle()



''' Problem 2: Zoo Animals
 Implement a class hierarchy using inheritance '''

class Animal():

    def __init__(self,name,category):

        self.name=name
        self.category=category
    def make_sound(self):
        pass

class Mammal(Animal):
    def make_sound(self):
        print(f"The {self.name} can make sound like- Haluum ")

    def give_birth(self,birth_year):
        self.birth_year=birth_year
        print(f"The {self.name} are {2023-self.birth_year} years old")

class Reptile(Animal):
    def make_sound(self):
        print(f"The {self.name} can make sound like- Sshii sshii")

    def lay_eggs(self):
        print(f"The {self.name} lays eggs.")

class Bird(Animal):
    def make_sound(self):
        print(f"The {self.name} can make sound like- Kicir Micir")
    def fly(self):
        print(f"The {self.name} can fly.")

class Lion(Mammal):
    pass
class Snake(Reptile):
    pass
class Eagle(Bird):
    pass

lion=Lion("Lion","mammal")
snake=Snake("Snack","reptile")
eagle=Eagle("Eagle","bird")
lion.make_sound()
snake.make_sound()
eagle.make_sound()

lion.give_birth(2000)
snake.lay_eggs()
eagle.fly()

