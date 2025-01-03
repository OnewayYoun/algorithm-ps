import random


class RandomizedSet:
    """
    Input
    ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    [[], [1], [2], [2], [], [1], [2], []]
    Output
    [null, true, false, true, 2, true, false, 2]
    """

    def __init__(self):
        self.container_dict = {}
        self.container_list = []

    def insert(self, val: int) -> bool:
        if val not in self.container_dict:
            self.container_list.append(val)
            self.container_dict[val] = len(self.container_list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.container_dict:
            idx = self.container_dict[val]
            last_idx = self.container_dict[self.container_list[-1]]
            self.container_dict[self.container_list[-1]] = idx
            del self.container_dict[val]
            self.container_list[idx], self.container_list[last_idx] = self.container_list[last_idx], \
            self.container_list[idx]
            self.container_list.pop()

            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.container_list)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.getRandom())
