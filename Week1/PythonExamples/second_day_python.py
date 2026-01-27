from abc import ABC, abstractmethod

#from yesteryday with functions

# you can even add functions as arguments in your functions
def called_function():
    return "this is called by the outter function"

def calls_outer_function(func1):
    return func1()

print(calls_outer_function(called_function))
#leave off the parentheses when passing in the function as an argument

# basic class syntax if the class keyword, ClassName:, init under method (add instance variables here), then associated function

class MyNewClass:
    #this sets up he constructor for the class. There can only be one
    #notice you can set default values for the parameteres by declaring them within the ()
    def __init__(self, age = 0, name ="default name"):
        self.name = name 
        self.age = age 

    def my_new_class_function(self): # first parameter is always a reference to self, doesn't have to be called self
        return f"My name is {self.name} and I am {self.age} years old."
    #note we should use self instead of jeeves, but this is just to illustrate the point

    # the __str__ method allows you to define what happens when you print an instance of the class
    def __str__(self):
        return f"MyNewClass(name={self.name}, age={self.age} from the to string method)"
    
    # the __repr__ method allows you to create a clone of the class. I could create a new variables and call this method to create a clone of the object
    def __repr__(self):
        return f"MyNewClass(self, {self.age},{self.name})"

# the self parameter is included because Python, under the hood, is actually using the class to call the function,
# and the particular object you want to use is being passed  as the first parameter

my_instance = MyNewClass(25, "Will")
print(my_instance.my_new_class_function())

my_class = MyNewClass()
print(my_class.__str__())
print(MyNewClass.__str__(my_class))  # equivalent to the above line
print(my_class)  # implicitly calls __str__()

#Python supports abstract classes. You make a class abstract by adding ABC inside the parentheses
class MyAbstractClass(ABC):

    #this is a class variable, accessed by calling the class itself, not an instantiated object
    class_count: int = 0

    #class methods take in the class as an implicity first argument,  can interact with and change the state of the class
    @classmethod
    def print_class_count(cls) -> int: 
        return cls.class_count
    #class methods take in the class as an implicity first argument,  can interact with and change the state of the class

    #static methods don't take in an implicit first argument, they behave like regular functions but belong to the class's namespace
    #static methods do not receive the class or an instance of the class as an implicit argument. You can add it,
    #but you might as well use a class method at that point
    @staticmethod
    def static_method_example():
        return "This is a static method example"


print(MyAbstractClass.class_count)
print(MyAbstractClass.print_class_count())
MyAbstractClass.static_method_example()
