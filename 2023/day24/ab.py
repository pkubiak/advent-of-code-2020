from copy import deepcopy
import fractions
import sympy as sym


def a(text: str):
    lines = text.split("\n")

    flakes = []
    for line in lines:
        pos, speed = line.split(" @ ")
        pos = list(map(int, pos.split(", ")))
        speed = list(map(int, speed.split(", ")))
        flakes.append((pos, speed))

    ile = 0
    for i in range(len(flakes)):
        for j in range(i+1, len(flakes)):
            f0, f1 = flakes[i], flakes[j]

            x0, vx0 = f0[0][0], f0[1][0]
            x1, vx1 = f1[0][0], f1[1][0]

            y0, vy0 = f0[0][1], f0[1][1]
            y1, vy1 = f1[0][1], f1[1][1]

            # x0 + tv0 = x1 + tv1
            # (x0 - x1) = t*(vx1 - vx0)

            # x0 + t0 * vx0 = x1 + t1 * vx1
            # t0 = (x1 + t1*vx1-x0)/vx0

            # y0 + t0 * vy0 = y1 + t1 * vy1
            # y0*vx0 + vy0*(x1 + t1*vx1-x0) = vx0*y1 + vx0*t1 * vy1
            # t1* = y0*vx0 + vy0*x1 - vy0*x0 - vx0*y1
            vvv  =vx0*vy1-vy0*vx1
            if vvv == 0:
                continue
            t1 = fractions.Fraction(y0*vx0 + vy0*x1 - vy0*x0 - vx0*y1, vvv)
            t0 = fractions.Fraction(y1 + t1*vy1 - y0, vy0)

            if t0 < 0 or t1 < 0:
                continue

            px = x1 + t1*vx1
            py = y1 + t1*vy1
            # print(t1, float(px), float(py))

            # if 7 <= px <= 27 and 7 <= py <= 27:
            if 200000000000000 <= px <= 400000000000000  and 200000000000000 <= py <= 400000000000000:
                ile += 1

    return ile 


def b(text: str):
    lines = text.split("\n")

    flakes = []
    for line in lines:
        pos, speed = line.split(" @ ")
        pos = list(map(int, pos.split(", ")))
        speed = list(map(int, speed.split(", ")))
        flakes.append((pos, speed))
    ###################
        
    sx = sym.Symbol('sx')
    sy = sym.Symbol('sy')
    sz = sym.Symbol('sz')

    vx = sym.Symbol('vx')
    vy = sym.Symbol('vy')
    vz = sym.Symbol('vz')

    t0 = sym.Symbol('t0')
    t1 = sym.Symbol('t1')
    t2 = sym.Symbol('t2')

    f0 = flakes[0]
    f1 = flakes[1]
    f2 = flakes[2]

    # t0 = f0[0][0]
    solution = sym.solve((
        t0 * vx + sx - t0 * f0[1][0] - f0[0][0],
        t1 * vx + sx - t1 * f1[1][0] - f1[0][0],
        t2 * vx + sx - t2 * f2[1][0] - f2[0][0],

        t0 * vy + sy - t0 * f0[1][1] - f0[0][1],
        t1 * vy + sy - t1 * f1[1][1] - f1[0][1],
        t2 * vy + sy - t2 * f2[1][1] - f2[0][1],

        t0 * vz + sz - t0 * f0[1][2] - f0[0][2],
        t1 * vz + sz - t1 * f1[1][2] - f1[0][2],
        t2 * vz + sz - t2 * f2[1][2] - f2[0][2],

    ), sx,sy,sz,t0,t1,t2,vx,vy,vz, dict=True)

    return solution[0][sx] + solution[0][sy] + solution[0][sz]
    # t0 * vx + sx = t0 * v0x + s0x
    # t1 * vx + sx = t1 * v1x + s1x
    # t2 * vx + sx = t2 * v2x + s2x

    # t0 * vy + sy = t0 * v0y + s0y
    # t1 * vy + sy = t1 * v1y + s1y
    # t2 * vy + sy = t2 * v2y + s2y

    # t0 * vz + sz = t0 * v0z + s0z
    # t1 * vz + sz = t1 * v1z + s1z
    # t2 * vz + sz = t2 * v2z + s2z

    # (t0-t1)*vx = t0*v0x + s0x + t1 * v1x + s1x

    # t0 * vy + sy = t0 * v0y + s0y


if __name__ == "__main__":
    def test(tests):
        for test_fn, fn, val in tests:
            res = fn(open(test_fn).read())
            if val is not None:
                assert res == val, f"{test_fn}: get {res!r} expected {val!r}"
            else:
                print(f"{fn.__name__}({test_fn}):", res)

    test([
        # ("test_a.txt", a, 12015),
        ("input.txt", a, None),
        ("test_a.txt", b, 47),
        ("input.txt", b, None),
    ])
