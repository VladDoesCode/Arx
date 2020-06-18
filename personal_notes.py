# Lines 4 - 85 are an introduction to Classes and Objects in Python
# From this youtube video: https://www.youtube.com/watch?v=wfcWRAxRVBA

'''
-The order of which classes happen from top down:
1. Class (a blueprint from which you can make objects)
2. Variable (a variable containing all the info below.) "r1"
3. Object (what the methods and instance variables are stored in)
4. Methods (functions within objects) "introduceSelf()"
4.5. Instance Variables (attributes of the object)" name: "Jerry"
'''

'''
-How a class may look (logically) for creating Robot objects:
Class Robot:
- name:
- color:
- weight:
- introduceSelf()
    + ex.
      print("My name is " + name)

- Notice how the attributes do not have values,
- This is because a class does not refer to a specific object (robot).
'''

'''
- Real Class code for Robot:
class Robot:

    # You need to add self to every method inside of a class.
    def introduce_self(self):
        print("My name is " + self.name) # self. refers to an object.

- Code to run after the class:
+ Making an object (r1) from class (Robot)
r1 = Robot() # Creating object (r1) with the class (Robot)

r2 = Robot() # Creating object (r2) with the class (Robot)

+ To set the attributes you can do:
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r2.name = "Jerry"
r2.color = "blue"
r2.weight = 40

+ To run a Method (introduce_self()) on specific Objects (r1) and (r2)
r1.introduce_self()
    + This would print "My name is Tom"

r2.introduce_self()
    + This would print "My name is Jerry"
'''

'''
- To avoid having to write all this to set up attributes:
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

+ Make a constructor with (__init__) when defining the class (Robot)
Class Robot:
    # Reminder to include (self) as an attribute (even in the constructor)
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

+ Now to make objects (r1) and (r2) from our NEW class (Robot):
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

+ We can see how using this more efficient method would yield the same results:
r1.introduce_self()
    + This would print "My name is Tom"

r2.introduce_self()
    + This would print "My name is Jerry"
'''


# Next covering how multiple classes and objects can interact with eachother in Python Lines: 91 - 178
# From this video: https://www.youtube.com/watch?v=WOwi0h_-dfA

'''
- First lets establish from classes and objects we will be working with:
- Class 1
Robot
- name:
- color:
- weight:
introduce_self()

+ Object 1
r1
- name: "Tom"
- color: "red"
- weight: 30

+ Object 2
r2
- name: "Jerry"
- color: "blue"
- weight: 40

# On top of our Robot Class we will make one called (Person) with two objects.
- Class 2
Person
- name:
- personality:
- isSitting:
# This attribute (robotOwned) is a relationship showing which person owns which robot (from above)
- robotOwned:

sit_down()
stand_up()


+ Object 3
p1
- name: "Alice"
- personality: "aggressive"
- isSitting: False
- robotOwned: r2

+ Object 4
p2
- name: "Becky"
- personality: "talkative"
- isSitting: True
- robotOwned: r1

- Real Code for new Situation:

Class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
         
    def introduce_self(self):
        print("My name is " + self.name)

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

+ Now to add the second class and objects

class Person:
    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting
    
    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

p1 = Person("Alice", "aggressive", False) # Alice as the name, aggressive as personality and False as is_sitting
p2 = Person("Becky", "talkative", True)

# p1 owns r2 and p2 owns r2
p1.robot_owned = r2
p2.robot_owned = r1

# Now because we set these attributes (much like putting it into the __init__ attribute) we can access it the same.
p1.robot_owned.introduce_self() 
# this is the same as saying r2.introduce_self()
# This should print out 'My name is Jerry'
'''


# This next section of notes (lines: 185 - ) is from https://realpython.com/python3-object-oriented-programming/
# As there were no more videos apart of the previous series.


'''
- What Is Object-Oriented Programming (OOP)?
Object-oriented Programming, or OOP for short,
is a programming paradigm (a fancy word meaning we can classify organization in python)
which provides a means of structuring programs so that
properties (instance variables) and behaviors (methods) are bundled into individual objects.

For instance, an object could represent a person with a name property, age, address, etc.,
with behaviors like walking, talking, breathing, and running.
Or an email with properties like recipient list, subject, body, etc.,
and behaviors like adding attachments and sending.

'''
