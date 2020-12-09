import sys

data = []
def check(x):
    for a in range(25):
        for b in range(a+1, 25):
            if data[a] + data[b] == x:
                return True
    return False

for line in sys.stdin:
    x = int(line.strip())

    if len(data) == 25:
        if not check(x):
            print(x)
            break
        data = data[1:]
    
    data.append(x)
    

        
