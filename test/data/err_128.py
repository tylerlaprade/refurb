# `if` blocks are used to separate test cases
x = 1
y = 2

tmp = x
x = y
y = tmp

filler = 1
tmp = x
x = y
y = tmp

filler = 1
filler = 2
tmp = x
x = y
y = tmp

tmp = x
x = y
y = tmp
tmp = x
x = y
y = tmp


tmp = x
y = tmp
x = y

tmp = x
x = y
tmp = 1
tmp, x = x, tmp
y = tmp

from typing import TYPE_CHECKING

# See https://github.com/dosisod/refurb/issues/23
if not TYPE_CHECKING:
    x = tmp
    x = tmp
    x = tmp
