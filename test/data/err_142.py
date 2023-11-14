# these should match

s = {1, 2, 3}
for x in (1, 2, 3):
    s.discard(x)

for x in (1, 2, 3):
    s.add(x + 1)


# these should not

s.update(iter((1, 2, 3)))

num = 123

for _ in (1, 2, 3):
    s.add(num)

for x in (set(),):
    x.add(x)

# TODO: support unpacked tuples here
for x, y in ((1, 2), (3, 4)):
    s.add((x, y))
