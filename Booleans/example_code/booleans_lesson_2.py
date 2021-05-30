# Real Python Vide Course: Python Booleans
# by Cesar Aguilar
# Based on the article https://realpython.com/python-boolean/
# by Moshe Zadka

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
