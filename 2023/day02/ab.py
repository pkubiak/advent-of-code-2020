def parse(text):
    for line in text.split("\n"):
        header, games = line.split(": ")
        game_id = int(header.split(" ")[1])

        yield game_id, [
            [x.split(" ") for x in game.split(", ")]
            for game in games.split("; ")
        ]

    
def a(text: str) -> int:
    total = 0
    for game_id, games in parse(text):
        maxs = {"red":0, "green": 0, "blue": 0}
        for game in games:
            for val, color in game:
                maxs[color] = max(maxs[color], int(val))

        if maxs["red"] <= 12 and maxs["green"] <= 13 and maxs["blue"] <= 14:
            total += game_id

    return total


def b(text: str) -> int:
    total = 0
    for _, games in parse(text):
        maxs = {"red":0, "green": 0, "blue": 0}
        for game in games:
            for val, color in game:
                maxs[color] = max(maxs[color], int(val))

        total += maxs["red"] * maxs["green"] * maxs["blue"]

    return total


if __name__ == "__main__":
    for fn, val in [(a, 8), (b, 2286)]:
        name = fn.__name__
        res = fn(open(f"test_{name}.txt").read())
        assert res == val, f"{name}: {res} != {val}"

        print(f"{name}:", fn(open("input.txt").read()))
