# Assigning values to variables
Sarah, John, Milan = 12, 3, 7

print(Sarah)  # Outputs: 12
print(John)   # Outputs: 3
print(Milan)  # Outputs: 7

# Slicing a string
girlName = "Lea The Dragon is the best"
print(girlName[0:14])  # Outputs: 'Lea The Dragon'

# Formatting a sentence using placeholders
sentence = "%s is the most beautiful in the world and soon turns %d"
print(sentence % ("Lea", 17))  # Outputs: 'Lea is the most beautiful in the world and soon turns 17'

# 1. Add 15 and 30, then divide by 2
print((15 + 30) / 2)  # Outputs: 22.5

# 2. Initialize two variables and perform arithmetic operations
a = 10
b = 5
print(a + b)  # Addition: 15
print(a - b)  # Subtraction: 5
print(a * b)  # Multiplication: 50
print(a / b)  # Division: 2.0
print(a % b)  # Remainder: 0

# 3. Store your name in a variable
name = "Your Name"

# 4. Create three variables in one line
banana, apple, pineapple = "banana", "apple", "pineapple"

# 5. Print "Hello" ten times using arithmetic operators
print(10 * "Hello")  # Outputs: 'HelloHelloHelloHelloHelloHelloHelloHelloHelloHello'

# 6. Multiple assignment for name and age
name, age = "Anna", 25

# 7. Combine two strings into a third variable
string1 = "Good"
string2 = " Morning"
combinedString = string1 + string2
print(combinedString)  # Outputs: 'Good Morning'

# 8. Print the fourth letter of a string
word = "Python"
print(word[3])  # Outputs: 'h'

# 9. Print letters from index 0 to 5
print(word[0:5])  # Outputs: 'Pytho'

# 10. Print all letters from the first index until the end
print(word[1:])  # Outputs: 'ython'

# Working with lists
shoppingList = ["banana", "apples", "milk"]
shoppingList.append("Water")  # Add "Water" to the list
print(shoppingList)  # Outputs: ['banana', 'apples', 'milk', 'Water']

del shoppingList[2]  # Remove "milk" from the list
print(shoppingList)  # Outputs: ['banana', 'apples', 'Water']

# Concatenate two lists and repeat elements
shoppingList2 = ["bag", "skirt", "hat"]
print(shoppingList + shoppingList2)  # Outputs: ['banana', 'apples', 'Water', 'bag', 'skirt', 'hat']
print(2 * shoppingList2)  # Outputs: ['bag', 'skirt', 'hat', 'bag', 'skirt', 'hat']

# Find the maximum and minimum in a list of numbers
numList = [1, 6, 3, 9, 2]
print(max(numList))  # Outputs: 9
print(min(numList))  # Outputs: 1

# Working with dictionaries
data = {"Rachel": 17, "Rahul": 61, "Anna": 15}
print(data.keys())   # Outputs: dict_keys(['Rachel', 'Rahul', 'Anna'])
print(data.values()) # Outputs: dict_values([17, 61, 15])

# Function definition and usage
def helloworld():
    print("Hello World")

helloworld()  # Outputs: 'Hello World'

# Help documentation
print(help("Hello".upper))  # Displays help documentation for the 'upper' method

# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age

# Create an object from the class
p1 = Person("Bob", 22)
print(p1.getname())  # Outputs: 'Bob'
print(p1.getage())   # Outputs: 22
