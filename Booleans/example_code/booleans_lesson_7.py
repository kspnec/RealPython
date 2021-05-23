# Real Python Vide Course: Python Booleans
# by Cesar Aguilar
# Based on the article https://realpython.com/python-boolean/
# by Moshe Zadka

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



