# these should match

def f1():
    global x
    global y


def f3():
    global x
    global y
    global z


def f4():
    global x
    global y
    global x
    global y


def f2():
    x = y = z = 1

    def inner():
        nonlocal x
        nonlocal y

    def inner2():
        nonlocal x
        nonlocal y
        nonlocal z

    def inner3():
        nonlocal x
        nonlocal y
        nonlocal x
        nonlocal y


def f5():
    w = x = y = z = 1

    def inner():
        global w
        global x
        nonlocal y
        nonlocal z

    def inner2():
        global x
        nonlocal y
        nonlocal z


# these should not

def fx():
    x = y = 1

    def inner():
        global x
        nonlocal y

    def inner2():
        nonlocal x
        nonlocal y


def fy():
    global x
    global y

def fz():
    global x
