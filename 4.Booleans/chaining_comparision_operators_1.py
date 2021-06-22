def u():
    print("I am u")
    return 1

def v():
    print("I am v")
    return 2

def w():
    print("I am w")
    return 3

# here v() is evealuated 2 times.
print(u() < v() and v() < w())

# can avoid this by using in chaines.
print(u() < v() < w())