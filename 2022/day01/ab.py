with open("input.txt") as file:
    numbers = file.read().split("\n\n")
    numbers = [sum(int(i) for i in line.split("\n")) for line in numbers]
    numbers.sort()
    print("a:",numbers[-1])
    print("b:", sum(numbers[-3:]))

