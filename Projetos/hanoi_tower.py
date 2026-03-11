def hanoi_solver(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []

    rods = [source, auxiliary, target]
    moves = []

    def record():
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

    record()

    def solve(k, start, end, temp):
        if k == 1:
            disk = rods[start].pop()
            rods[end].append(disk)
            record()
            return

        solve(k-1, start, temp, end)

        disk = rods[start].pop()
        rods[end].append(disk)
        record()

        solve(k-1, temp, end, start)

    solve(n, 0, 2, 1)

    return "\n".join(moves)

print(hanoi_solver(2))