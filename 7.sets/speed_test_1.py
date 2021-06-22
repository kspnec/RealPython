def initialize_set():
    s = set()
    for i in range(1000):
        s.add(i)
    return s

def initialize_lst():
    lst = list()
    for i in range(1000):
        lst.append(i)
    return lst

def initialize_tup():
    tup = tuple()
    for i in range(1000):
        tup += (i,)
    return tup