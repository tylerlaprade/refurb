from itertools import count

nums = (1, 2, 3)

# these should match

for index, _ in enumerate(nums):
    print(index)

for num in nums:
    print(num)

_ = (index for index, _ in enumerate(nums))
_ = iter(nums)

_ = {"key": index for index, _ in enumerate(nums)}
_ = {"key": num for num in nums}

_ = (1 for num in nums)

_ = {"key": "value" for num in nums}

nums2 = [4, 5, 6]
nums3 = 7, 8, 9

_ = (index for index, _ in enumerate(nums3))


# "count" is an infinite generator. In general, we only want to warn on
# sequence types because you can call len() on them without exhausting some
# iterator.
counter = count()
_ = (num for index, num in enumerate(nums) if index)
