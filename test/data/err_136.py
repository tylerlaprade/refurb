x = 1
y = 2

# these should match

_ = min(x, y)
_ = min(x, y)
_ = max(x, y)
_ = max(x, y)

_ = max(y, x)
_ = max(y, x)
_ = min(y, x)
_ = min(y, x)

# these should not

z = 3

_ = x if x < y else z
