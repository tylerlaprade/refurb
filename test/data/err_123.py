# these will match

_ = True
_ = bytes(b"hello world")
_ = complex(1j)
_ = dict({"a": 1})
_ = 123.456
_ = [1, 2, 3]
_ = "hello world"
_ = 1, 2, 3
_ = 123

a = True
_ = a

b = b"hello world"
_ = bytes(b)

c = 1j
_ = complex(c)

d = {"a": 1}
_ = dict(d)

e = 123.456
_ = e

f = [1, 2, 3]
_ = list(f)

g = "hello world"
_ = g

t = (1, 2, 3)
_ = tuple(t)


# these will not

_ = bool([])
_ = bytes(0xFF)
_ = complex(1)
_ = dict((("a", 1),))
_ = float(123)
_ = [1, 2, 3]
_ = str(123)
_ = 1, 2, 3
_ = int("0xFF")
