from enum import Enum

class Choice(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

    def cmp(self, other) -> int: # -1, 0, 1
        if other == self:
            return 0
        return -1 if self.value%3 + 1 == other.value else 1

    def score(self, other) -> int:
        return self.value + 3 * (self.cmp(other)+1)


MAPPING = {
    "A": "Rock", "B": "Paper", "C": "Scissors",
    "X": "Rock", "Y": "Paper", "Z": "Scissors"
}

def translate_a(opponent: str, me: str):
    return Choice[MAPPING[me]], Choice[MAPPING[opponent]]


def translate_b(opponent: str, me: str):
    a = Choice[MAPPING[opponent]]
    b = {"X": -1, "Y": 0, "Z": 1}[me]
    b = [i for i in Choice if i.cmp(a) == b][0]
    return b, a


if __name__ == "__main__":
    with open("input.txt") as file:
        items = [line.strip().split(" ") for line in file]

    print("a:", sum(Choice.score(*translate_a(*item)) for item in items))
    print("b:", sum(Choice.score(*translate_b(*item)) for item in items))
