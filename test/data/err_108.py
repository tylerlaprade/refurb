x = y = "abc"

class C:
    y: str = "xyz"

c = C()


# these should match

_ = x in {"abc", "def"}
_ = c.y in ["abc", "def"]
_ = x in {"abc", "def", "ghi"}
_ = x == "abc" or x == "def" or y == "ghi"

_ = x in {"abc", "def"}

_ = x in {"abc", "def"}
_ = x in {"abc", "def"}
_ = x in {"abc", "def"}

# these should not

_ = x == "abc" or y == "def"
_ = x == "abc" or x == "def" and y == "ghi"
