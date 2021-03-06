class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person({self.name})'

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
