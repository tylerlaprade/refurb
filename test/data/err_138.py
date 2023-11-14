# these should match

def f1():
    arr = [1, 2, 3]


def f2():
    arr = [num + 1 for num in (1, 2, 3)]


def f3():
    arr = [num for num in (1, 2, 3) if num % 2]


nums = [num for num in (1, 2, 3) if num % 2]


# should not match

def f4():
    arr = [1, 2, 3]


def f5():
    arr = []

    for num in (1, 2, 3):
        arr.pop(num)


def f6():
    arr = []

    arr2 = [1, 2, 3]


def f7():
    arr = []

    for num in (1, 2, 3):
        if x := num + 1:
            arr.append(x)


def f8():
    s = "abc"

    for num in (1, 2, 3):
        s.append(num)


def f9():
    arr = [1, 2, 3]


def f10():
    arr = [1, 2, 3]

    arr.extend(iter((1, 2, 3)))


def f11():
    arr = []

    for num in (1, 2, 3):
        if num not in arr:
            arr.append(arr)


def f12():
    arr = []

    arr.extend(arr for _ in (1, 2, 3))
