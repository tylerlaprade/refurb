b = True

# these should match

_ = b
_ = not b
_ = not b
_ = b
_ = True is b
_ = False is b

_ = b
_ = not b
_ = not b
_ = b
_ = b
_ = not b


# these should not

class C:
    def __bool__(self) -> bool:
        return False

_ = C() is True

def f() -> bool | None:
    return None

x: bool | None = f()

_ = x is True

_ = b is b
_ = b is not b
