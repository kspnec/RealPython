# Basic usage

demo_string = "This is a demonstration of the {} function".format("format")
# Expected output: 'This is a demonstration of the format function'
# print(demo_string)

fruits = ["apples", "bananas", "oranges"]
# You can use indices to access lists in format strings
# The '0' below refers to the 0th argument
fruit_demo_string = "My favorite fruits are {0[1]}".format(fruits)
# Expected output: 'My favorite fruits are bananas' 
# print(fruit_demo_string)

vegetables = {
    'carrots': 5,
    'tomatoes': 3,
    'brussel sprouts': 7,
}
# Dictionary keys work too!
vegetable_demo_string = "Carrots are tasty, and they only cost ${0[carrots]} per pound!".format(vegetables)
# Expected output: 'Carrots are tasty, and they only cost $5 per pound!'
# print(vegetable_demo_string)

# Basic keyword argument -- experiment with more exciting kwargs on your own!
colors = ['red', 'blue', 'green']
color_demo_string = "The best color has to be {red}".format(red=colors[0])
# Expected output: 'The best color has to be red'
# print(color_demo_string)