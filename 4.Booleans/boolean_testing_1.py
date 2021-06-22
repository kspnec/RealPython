# examples shows how objects are converted to Booleans:

def message(msg=None):
    return msg or "This action can't be undone!"

# here we use or to print the default values.

print(message())

print(message("Are you sure?"))

