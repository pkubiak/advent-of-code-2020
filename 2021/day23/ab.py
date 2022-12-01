"""
States:
    I: Initial place
    F: Final location

positions:
    01.3.5.7.910
      2 4 6 8
"""
from functools import cache

STEP_ENERGY = {"A": 1, "B": 10, "C": 100, "D": 1000}


def can_move(state, from_x, to_x):
    for i in state:
        if isinstance(i, int):
            if to_x <= i < from_x or from_x < i <= to_x:
                return False
    return True


def get_moves(types, state):
    height = len(state) // 4

    for room_x in range(4):
        for room_y in range(height):
            if room_y > 0 and state[4*(room_y-1) + room_x] == 'I':
                break

            i = 4*room_y + room_x

            if state[i] == 'F':
                continue

            if state[i] == 'I':
                pos_x = 2*(i%4) + 2
                for dest in [0, 1, 3, 5, 7, 9, 10]:
                    if can_move(state, pos_x, dest):
                        steps = abs(dest-pos_x) + room_y + 1
                        new_state = state[:i] + (dest,) + state[i+1:]
                        yield (STEP_ENERGY[types[i]] * steps, new_state)
            else:
                pos_x = state[i]

            ## Try to move final position
            final_room_x = 'ABCD'.index(types[i])

            occupied = [final_room_x + 4*z for z in range(height) if state[final_room_x + 4*z] == 'I' and types[final_room_x+4*z] != types[i]]

            if occupied: # there is other amphipods in our room
                continue

            if state[i] == 'I' and final_room_x == room_x:
                if any(state[room_x+4*ii] != 'F' for ii in range(room_y+1, height)): # mamy coś pod sobą
                    continue
                # jesteśmy już we właściwym pokoju
                new_state = state[:i] + ('F', ) + state[i+1:]
                yield (0, new_state)
                continue


            dest = 2 * final_room_x + 2
            if not can_move(state, pos_x, dest):
                continue

            ile = sum(types[ii] == types[i] and state[ii] == 'F' for ii in range(len(state)))
            steps = abs(dest-pos_x) + (room_y + 1 if state[i] == 'I' else 0) + (height - ile)
            new_state = state[:i] + ('F',) + state[i+1:]
            yield (STEP_ENERGY[types[i]] * steps, new_state)


@cache
def find(types, state):
    if state.count('F') == len(state):
        return 0

    best = 2**40

    for move_cost, new_state in get_moves(types, state):
        total_cost = find(types, new_state) + move_cost
        best = min(best, total_cost)
    
    return best


def part_a(conf):
    return find(conf, ('I',) * len(conf))

def part_b(conf):
    conf = conf[:4] + 'DCBADBAC' + conf[4:]
    return part_a(conf)

if __name__ == '__main__':
    conf = 'DCDBBAAC'
    # conf = 'BCBDADCA'

    print("a:", part_a(conf))
    print("b:", part_b(conf))
