# these should match

with open("file.txt") as f:
    pass
with open("file.txt") as f:
    lines = [f"{line}!" for line in f.readlines()]


with open("file.txt") as f:
    lines = [f"{line}!" for line in f.readlines()]


with open("file.txt", "rb") as f:
    lines = [f"{line}!" for line in f.readlines()]


f = open("file.txt")
# these will not

with open("file.txt") as f:
    for _ in f.readlines(1):
        pass


with open("file.txt") as f:
    pass


class Reader:
    @staticmethod
    def readlines() -> list[str]:
        return ["hello", "world"]

for _ in Reader.readlines():
    pass


file = open("file.txt")
x = file.readlines()
