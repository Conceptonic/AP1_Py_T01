from collections import defaultdict

try:
    first_line = input().split()
    if len(first_line) != 2:
        raise ValueError
    n, target = int(first_line[0]), int(first_line[1])
    if n <= 0 or target <= 0:
        raise ValueError

    by_year = defaultdict(list)
    for _ in range(n):
        parts = input().split()
        if len(parts) != 3:
            raise ValueError
        year, cost, time = int(parts[0]), int(parts[1]), int(parts[2])
        if year <= 0 or cost <= 0 or time <= 0:
            raise ValueError
        by_year[year].append((cost, time))

except ValueError:
    print("Invalid input")
else:
    best = None
    for devices in by_year.values():
        for i in range(len(devices)):
            for j in range(i + 1, len(devices)):
                c1, t1 = devices[i]
                c2, t2 = devices[j]
                if t1 + t2 == target:
                    total = c1 + c2
                    if best is None or total < best:
                        best = total

    print(best)