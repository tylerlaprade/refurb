# these should match

nums = [1, 2, 3]
authors = {"Dune": "Frank Herbert"}
primes = {1, 2, 3, 5, 7}
data = (True, "something", 123)
name = "bob"
fruits = frozenset(("apple", "orange", "banana"))


if not nums: ...
if not authors: ...
if not primes: ...
if not data: ...
if not name: ...
if not fruits: ...

if len(nums) <= 0: ...
if nums:
    ...
    ...
    ...
...
...
...
...
if not set(()): ...
if not frozenset(()): ...

if not nums: ...

match 1:
    case 1 if not nums:
        pass

_ = [x for x in () if not nums]
_ = (x for x in () if not nums)
_ = {"k": v for v in () if not nums}

_ = 1 if not nums else 2

while not nums:
    pass

assert not nums


# len(x)

if len(nums): ...

match 1:
    case 1 if len(nums):
        pass

_ = [x for x in () if len(nums)]
_ = (x for x in () if len(nums))
_ = {"k": v for v in () if len(nums)}

_ = 1 if len(nums) else 2

while len(nums):
    pass

assert len(nums)

assert not nums
assert nums != []

assert not authors
assert authors != {}


# these should not

if len(nums) == 1: ...
if len(nums) != 1: ...

x = not nums


# We cannot verify all containers. For example, with this container, the length
# does not indicate whether it is truthy or not.
class Container:
    def __bool__(self) -> bool:
        return False

    def __len__(self) -> int:
        return 1337

container = Container()

if len(container) == 0: ...

if print(len(nums) == 0): ...
if (lambda: len(nums) == 0)(): ...

assert nums == [1, 2, 3]
assert authors == {"author": "book"}
assert nums <= []
