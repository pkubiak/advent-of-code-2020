import sys
labeling = sys.stdin.read().strip()


for i in range(100):
    current = labeling[0]
    # print(i+1, current, labeling)
    labeling = labeling[1:] + labeling[0]
    three = labeling[:3]
    labeling = labeling[3:]

    destination = int(labeling[-1])
    while True:
        destination = (destination - 2)%9 + 1
        if str(destination) in labeling:
            break
    j = labeling.index(str(destination))
    labeling = labeling[:j+1] + three + labeling[j+1:]

    j = labeling.index(current)
    labeling = labeling[j+1:] + labeling[:j+1]

j = labeling.index('1')
labeling = labeling[j+1:] + labeling[:j]
print(labeling)