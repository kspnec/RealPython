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


def initialize_tuple():
    tup = tuple()
    for i in range(1000):
        tup += (i,)
    return tup


s = initialize_set()
lst = initialize_lst()
tup = initialize_tuple()


def membership_set():
    for i in range(1000):
        i in s


def membership_lst():
    for i in range(1000):
        i in lst


def membership_tuple():
    for i in range(1000):
        i in tup
