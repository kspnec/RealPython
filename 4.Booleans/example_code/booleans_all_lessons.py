# Real Python
# Python Booleans
# Video Course by Cesar Aguilar
# Based on the article https://realpython.com/python-boolean/
# by Moshe Zadka

#%% Lesson 1
issubclass(bool, int)
isinstance(True, bool)
isinstance(False, bool)
isinstance(1, bool)
isinstance(0, bool)

import keyword
print(keyword.kwlist)

int(True)
int(False)

True + True + False + True

codes = [264, 118, 543, 705, 1152, 674]
N = 3

[c % N == 0 for c in codes]

sum([c % N == 0 for c in codes])



#%% Lesson 2
not True
not False
not 1
not 0
not 'hello world'
not ''
not [1, 2, 3]
not []

first_name = ""
if not first_name:
    first_name = "Not given"
    
print(first_name)

first_name = "Luigi"
if not first_name:
    first_name = "Not given"
    
print(first_name)

first_name = ""
first_name = "Not given" if not first_name else first_name
print(first_name)

first_name = "Luigi"
first_name = "Not given" if not first_name else first_name
print(first_name)


#%% Lesson 3
from itertools import product
for x, y in product([True, False], repeat=2):
    print(f"\t{x} and {y} = {x and y}")
    
def print_and_return(x):
    print(f"\tI am returning {x}")
    return x

True and print_and_return(False)
True and print_and_return(True)

True and print_and_return(2/3)
#True and print_and_return(1/0)

False and print_and_return(True)
False and print_and_return(1/0)


#%% Lesson 4
from itertools import product
for x, y in product([True, False], repeat=2):
    print(f"\t{x} or {y} = {x or y}")
    
    
def print_and_return(x):
    print(f"\tI am returning {x}")
    return x

True or print_and_return(False)
True or print_and_return(1/0)

False or print_and_return(5)
#False or print_and_return(1/0)

first_name = ""
not first_name

first_name = ""
first_name = first_name or "Not given"
print(first_name)

first_name = "Luigi"
first_name = first_name or "Not given"
print(first_name)


#%% Lesson 5
print(1 == 1)
print(True == 1)
print(1.0 == 1)
print(1 + 0j == 1)
print(4/2 == 2)
print('1' == 1)

print(2 == [1, 2, 3])
print([1, 2, 3] == [1, 2, 3])
print({1, 2, 3} == {3, 1, 2})

print(0.25 + 0.25 == 0.5)

print(0.2 + 0.1 == 0.3)

x = 0.1

print(f"{x:.50f}")

print(1.0 < 3)

print([4, 0] >= [3, 2000000, 5000000])

print([4, 0] >= [4.1, 2000000, 5000000])

# returns TypeError
#print([1, 2, 3] < {4, 5, 6})

print(1.0 < 3)

a = {"x": 1, "y": 2}
b = {"x": 3, "y": 4}

# returns TypeError
# print(a < b)

print({1, 2, 3} < {4, 5, 6})
print({4, 5, 6} < {1, 2, 3})
print({4, 5, 6} == {1, 2, 3})
print({4, 5, 6} >= {1, 2, 3})
print({4, 5, 6} != {1, 2, 3})

x, y = [1, 2, 3], [1, 2, 3]

print(x == y)

id(x)
id(y)

print(x is y)

z = x

print(x == z)

id(z)
id(x)

print(x is z)
print(z is x)

print(1 in [1, 2, 3])

print("luigi" in {"luigi", "mario", "yoshi"})

print("luigi" in "luigi mario yoshi")

print("bowser" in "luigi mario yoshi")

d = {"a": 1, "b": 3}

print("c" in d)
print("b" in d)
print("b" not in d)


#%% Lesson 6
def  u():
    print("I am u")
    return 1

def  v():
    print("I am v")
    return 2

def  w():
    print("I am w")
    return 3

u() < v()

v() < w()

u() < v() and v() < w()

u() < v() < w()


#%% Lesson 7
def func():
    return False

bool(func)

class Article:
    pass

article = Article()
bool(article)

class Article:
    published = False
    
    def __bool__(self):
        return self.published
    
article = Article()
bool(article)

article.published = True
bool(article)


if article:
    print("The article has been published")
    
class Graph:
    vertices = []
    
    def __len__(self):
        return len(self.vertices)
    

airports = Graph()
bool(airports)

airports.vertices = ["jfk", "lax", "mia"]

bool(airports)

if airports:
    print(airports.vertices)
    
    
airports.vertices = []

if airports:
    print(airports.vertices)
    
    
class User:
    active = False
    posts = []
    
    def __len__(self):
        return len(self.posts)
    
    def __bool__(self):
        return self.active
    

user = User()
user.posts = ["Great picture!", "Thank you!"]

if user:
    print("We have an active user!")
else:
    print("We have an inactive user!")
    
user.active = True
if user:
    print("We have an active user!")
else:
    print("We have an inactive user!")

