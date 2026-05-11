from collections import deque

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, 'input.txt')) as f:
    matrix = [list(map(int, line.split())) for line in f if line.strip()]

n = len(matrix)
visited = [[False] * n for _ in range(n)]
squares = 0
circles = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and not visited[i][j]:
            cells = []
            queue = deque([(i, j)])
            visited[i][j] = True
            while queue:
                r, c = queue.popleft()
                cells.append((r, c))
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

            min_r = min(r for r, c in cells)
            max_r = max(r for r, c in cells)
            min_c = min(c for r, c in cells)
            max_c = max(c for r, c in cells)

            cell_set = set(cells)
            is_square = all(
                (r, c) in cell_set
                for r in range(min_r, max_r + 1)
                for c in range(min_c, max_c + 1)
            )

            if is_square:
                squares += 1
            else:
                circles += 1

print(squares, circles)
