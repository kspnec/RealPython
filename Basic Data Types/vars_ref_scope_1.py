num = [1, 2, 3, 4, 5]
print(dir(num))


a = 1
b = 'global'
c = 'another global'

def function():
    a = 2
    b = 'local'
    print(a, b)
    # vars() will show all the variables available for this function.
    # i.e (local variables)
    # Dictionary format.
    print(vars())
    # you can also use globals() function which gives global variables at any point. 
    print(globals())
    # if the variable is not defined in local scope, then 
    # it will refer the global variables value.
    print(c)

print(a, b)
function()
print(a, b)
# shows vars in global variables.
print(vars())
# you can also use globals() function which gives global variables at any point. 
print(globals())

# its not a good idea to name your local variables 
# with same name as global variables.