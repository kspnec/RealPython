# Real Python Vide Course: Python Booleans
# by Cesar Aguilar
# Based on the article https://realpython.com/python-boolean/
# by Moshe Zadka

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