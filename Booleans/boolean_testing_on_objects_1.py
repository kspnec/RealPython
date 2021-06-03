# Convernt objects into booleans for efficient python codes.

class Dummy():
    pass

a = Dummy()
print(bool(a))
# this returns True.

class Article():
    published = False
    # dunder bool method will return the article is published or not.
    def __bool__(self):
        return self.published

# article is the instance of Article() class.
article = Article()
print(bool(article))

article.published = True
print(bool(article))

if article:
    print("This article has been published!") 

# define Graph class.
class Graph():
    # Grap is going to have list of verticies. empty list initially.
    vertices = []
    # dunder lenght method going to return no. of vertices in the graph.
    def __len__(self):
        return len(self.vertices)

airports = Graph()
# currently the airport instance 
# of the Graph() class - the length of vertices is 0.
print(bool(airports))

airports.vertices = ["jfk", "lax", "mia"]
print(bool(airports))

if airports:
    print(airports.vertices)

airports.vertices = []
if airports:
    # vertices are empty list, Thus if statement will return False. 
    # so it won't print anything.
    print(airports.vertices)

# example: 3
# this class has both dunder __bool__ and __int__ methods defined.
class User():
    # defining two properties for user is active ?
    # and posts made by him on our website.
    active = False
    posts = []
    def __bool__(self):
        return self.active
    def __len__(self):
        return len(self.posts)
    
user = User()
user.posts = ["Great picture!", "Thank you!"]

print(user.active)

# these both will return the lenght of posts.
print(len(user))
print(len(user.posts))

if user:
    print("we have an active user!")
else:
    print("we have an inactive user")

# now if we change the active property
user.active = True
if user:
    print("we have an active user!")
else:
    print("we have an inactive user")
