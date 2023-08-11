class Joystick:
    def __init__(self, name: str):
        self.name: str = name
        self.number_of_alphabet: int = 26
        self.length: int = len(name)

    def simulate(self) -> int:
        up_and_down_cnt = sum(map(self.min_up_and_down, self.name.replace('A', '')))
        left_and_right_cnt = self.min_left_and_right()
        return up_and_down_cnt + left_and_right_cnt

    def min_up_and_down(self, letter: str) -> int:
        return min(ord(letter) - ord('A'), ord('A') + self.number_of_alphabet - ord(letter))

    def min_left_and_right(self) -> int:
        min_val = float('inf')
        for idx, letter in enumerate(self.name):
            next_ = idx + 1
            while next_ < self.length and self.name[next_] == 'A':
                next_ += 1
            min_val = min(min_val, 2 * idx + self.length - next_)
            min_val = min(min_val, idx + (self.length - next_) * 2)
        return min_val


def solution(name):
    joystick = Joystick(name)
    return joystick.simulate()


if __name__ == '__main__':
    print(solution('JEROEN'))  # 56
    print(solution('JAN'))  # 23
