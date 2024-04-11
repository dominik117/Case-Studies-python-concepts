class Person:
    age = 25

    @classmethod
    def printAge(cls):
        # cls refers to the class Person
        print('The age is:', cls.age)

# Class method called using class name
Person.printAge()  # Output: The age is: 25


class Mathematics:

    @staticmethod
    def addNumbers(x, y):
        return x + y

# Static method called using class name
print('The sum is:', Mathematics.addNumbers(5, 10))  # Output: The sum is: 15

class MyClass:
    class_attribute = 0
    global_attribute = 0

    @classmethod
    def increment_class_attribute(cls):
        cls.class_attribute += 1

MyClass.increment_class_attribute()
MyClass.increment_class_attribute()

print(MyClass.class_attribute)  # Output: 2



"""
Why Use Them?

Class Methods:
For methods that need to access the class attribute.
Common use is for factory methods that return an instance of the class.
To provide different ways of creating an object.

Static Methods:
When you don't need access to the class or instance properties but still want a method to be part of the class's namespace.
Grouping utility functions to a class, which can improve code organization and readability.
"""