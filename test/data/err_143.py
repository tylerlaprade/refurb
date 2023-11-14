s = set()
f = frozenset()
l = []
d = {}
t = ()
t2 = (1, )
r = ""
b = b""
n = False
i = 0

# these should match

_ = s or set()
_ = f or frozenset()
_ = l or []
_ = d or {}
_ = t or ()
_ = t2 or ()
_ = r or ""
_ = b or b""
_ = n or False
_ = i or 0


class C:
    x: int
    def __init__(self) -> None:
        # x could be anything here
        self.x = 123

c = C()

_ = c.x or 0


# these should not

_ = s or {1, 2, 3}
_ = f or frozenset((1, 2, 3))
_ = l or [1, 2, 3]
_ = d or {"a": "b"}
_ = t or (1, 2, 3)
_ = t2 or (1, 2, 3)
_ = r or "abc"
_ = b or b"abc"
_ = n or True
_ = i or 123
