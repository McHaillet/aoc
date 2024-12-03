from operator import mul
from functools import partial


with open("input.txt") as f:
    wire_1 = f.readline().strip().split(',')
    wire_2 = f.readline().strip().split(',')

move_to_op = {
    'R': partial(mul, 1),
    'L': partial(mul, -1),
    'U': partial(mul, 1j),
    'D': partial(mul, -1j),
}


def intersect(p1, p2, p3, p4):
    t_num = (
        (p1.real - p3.real) * (p3.imag - p4.imag) -
        (p1.imag - p3.imag) * (p3.real - p4.real)
    )
    t_denom = (
        (p1.real - p2.real) * (p3.imag - p4.imag) -
        (p1.imag - p2.imag) * (p3.real - p4.real)
    )
    t = t_num / t_denom if t_denom != 0 else 0
    u_num = (
        (p1.real - p2.real) * (p1.imag - p3.imag) -
        (p1.imag - p2.imag) * (p1.real - p3.real)
    )
    u_denom = (
        (p1.real - p2.real) * (p3.imag - p4.imag) -
        (p1.imag - p2.imag) * (p3.real - p4.real)
    )
    u = - (u_num / u_denom) if u_denom != 0 else 0
    if 0 < t < 1 and 0 < u < 1:
        return (
            p1.real + t * (p2.real - p1.real) +
            1j * (p1.imag + t * (p2.imag - p1.imag))
        )
    else:
        None


w1_start = 0
intersections = []
for m1 in wire_1:
    w1_end = w1_start + move_to_op[m1[0]](int(m1[1:]))
    w2_start = 0
    for m2 in wire_2:
        w2_end = w2_start + move_to_op[m2[0]](int(m2[1:]))
        res = intersect(w1_start, w1_end, w2_start, w2_end)
        if res is not None:
            intersections.append(res)
        w2_start = w2_end
    w1_start = w1_end

print(f"part 1: {int(min(abs(x.real) + abs(x.imag) for x in intersections))}")