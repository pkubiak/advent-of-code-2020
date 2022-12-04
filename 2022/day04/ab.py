with open("input.txt") as file:
    count_a = count_b = 0
    for line in file:
        a0, a1, b0, b1 = map(int, line.replace(",","-").split("-"))

        if a0 <= b0 <= b1 <= a1 or b0 <= a0 <= a1 <= b1:
            count_a += 1
        
        if not (a1 < b0 or b1 < a0):
            count_b += 1

print("a:", count_a)
print("b:", count_b)