# these will match

def is_even(x):
    return x % 2 == 0


def is_even_again(x):
    match x % 2:
        case 0:
            return True

        case _:
            return False

def nested(x):
    match x % 2:
        case 0:
            return True

        case _:
            match x % 3:
                case 0:
                    return True

                case _:
                    return False

def match_multiple_stmts(x):
    match x:
        case 1:
            return 1

        case 2:
            return 2

        case _:
            return 3


# these will not

def func(x):
    return x == 1

def func2(x):
    match x % 2:
        case 0:
            return True

        case _:
            return False

def func3(x):
    match x % 2:
        case 0:
            return True

    return False

def func4(x):
    return x == 1

def func5():
    return False

def func6(x):
    match x:
        case 1:
            return 1

        case 2:
            return 2

def func7(x):
    match x:
        case 1:
            pass

        case _:
            return 2

def func8(x):
    if x != 1:
        return 1
