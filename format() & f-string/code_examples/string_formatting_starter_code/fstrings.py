# Basic usage of fstrings
# Make sure you're using Python 3.5+!

function_name = "format"
demo_string = f"This is a demonstration of the {function_name} function"
# Expected output: 'This is a demonstration of the format function'
# print(demo_string)

fruits = ["apples", "bananas", "oranges"]
# You can use indices to access lists in f-strings
fruit_demo_string = f"My favorite fruits are {fruits[1]}"
# Expected output: 'My favorite fruits are bananas' 
# print(fruit_demo_string)

# With f-strings, you can easily add some random choice!
import random
fruit_demo_string = f"My favorite fruits are (Randomized) {random.choice(fruits)}"
# Expected output: 'My favorite fruits are (Randomized) ??'
# print(fruit_demo_string)

vegetables = {
    'carrots': 5,
    'tomatoes': 3,
    'brussel sprouts': 7,
}
# Dictionary keys work too! (Note the use of quotes in the dict key as compared to with .format())
vegetable_demo_string = f"Carrots are tasty, and they only cost ${vegetables['carrots']} per pound!"
# Expected output: 'Carrots are tasty, and they only cost $5 per pound!'
# print(vegetable_demo_string)

# With f-strings, it's even easier to do arbitrary computations within a string
time_demo_string = f"There are {1000 * 60 * 60 * 24} milliseconds in a day!"
# print(time_demo_string)

# And you have a host of formatting options available to you, just like with format strings.