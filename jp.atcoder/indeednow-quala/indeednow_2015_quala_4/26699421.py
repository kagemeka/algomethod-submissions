import typing
import sys


def main() -> typing.NoReturn:
    h, w = map(int, input().split())
    a = list(map(int, sys.stdin.read().split()))

    gy = [-1] * (h * w)
    gx = [-1] * (h * w)
    for i in range(1, h * w):
        gy[i], gx[i] = divmod(i - 1, w)
    gy[0], gx[0] = h - 1, w - 1

    def hf(i: int, v: int) -> int:
        y, x = divmod(i, w)
        return abs(gy[v] - y) + abs(gx[v] - x)

    heu = sum(hf(i, v) for i, v in enumerate(a) if v != 0)
    max_cost = 24
    que = [set() for _ in range(max_cost + 3)]
    que[heu].add((heu, tuple(a)))
    dyx = ((-1, 0), (0, -1), (1, 0), (0, 1))

    def on_board(y: int, x: int) -> bool:
        return 0 <= y < h and 0 <= x < w

    for score in range(max_cost + 1):
        while que[score]:
            hu, u = que[score].pop()
            cu = score - hu
            if hu == 0:
                print(cu)
                return
            i = u.index(0)
            y, x = divmod(i, w)
            for dy, dx in dyx:
                ny, nx = y + dy, x + dx
                if not on_board(ny, nx): continue
                j = ny * w + nx
                hv = hu + hf(i, u[j]) - hf(j, u[j])
                v = list(u)
                v[i], v[j] = v[j], v[i]
                que[cu + 1 + hv].add((hv, tuple(v)))

main()
