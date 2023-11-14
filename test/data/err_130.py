# these should match

d = {}

x = "key"


class NotADict:
    def keys(self) -> list[str]:
        return ["abc"]


not_a_dict = NotADict()

if "key" in not_a_dict.keys():
    pass
