from abc import ABC, abstractmethod
from collections import namedtuple


class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


# animal: parent base class
# mammal: child sub class
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal constructor")
        self.weight = 3

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


m = Mammal()
print(m.eat())
print("Age is", m.age)
print("Weight is", m.weight)
print(isinstance(m, Animal))
print(issubclass(Mammal, Animal))


# Multiple inherretance
class Employee:
    def greet(self):
        print("Hello Employee")


class Person:
    def greet(self):
        print("Hello Person")


class Manager(Employee, Person):
    pass


m = Manager()
m.greet()


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True
        print("Stream opened")

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False
        print("Stream closed")

    @abstractmethod
    def read(self):
        pass

    # def


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from MemoryStream")


stream = MemoryStream()
stream.open()
stream.read()
stream.close()


# Polymorphism
# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class TextBox(UIControl):
class TextBox():
    def draw(self):
        print("TextBox")


# class DropDownList(UIControl):
class DropDownList():
    def draw(self):
        print("Drop Down")


# def draw(control):
#     control.draw()

def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
# draw(ddl)
# print(isinstance(ddl, UIControl))
textbox = TextBox()
# draw(textbox)
draw([ddl, textbox])


class Text(str):
    def duplicate(self):
        return self + self


text = Text("Hello")
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


my_list = TrackableList()
my_list.append("1")


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
print(p1.x)
p2 = Point(x=1, y=2)
print(p1 == p2)
