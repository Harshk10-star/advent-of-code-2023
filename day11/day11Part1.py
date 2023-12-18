from collections import deque
def expand_glaxsy(grid):
    rows = []
    cols = []
    N = len(grid)
    M = len(grid[0])
    for i in range(N):
        isEmptyRow = True

        # row check
        for j in range(M):
            if grid[i][j] != '.':
                isEmptyRow = False
                break
        if isEmptyRow:
            rows.append(i)

    for i in range(M):
        isEmptyCol = True
        # col check

        for j in range(N):

            if grid[j][i] != '.':
                isEmptyCol = False
                break
        if isEmptyCol:
            cols.append(i)

    return rows, cols

def bfs(grid, starting, visitedG, rows, cols):
    q = deque()
    q.append([starting[0], starting[1], 0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    ans = 0
    visited = set()
    visited.add((starting[0], starting[1]))
    while q:
        for _ in range(len(q)):
            x, y, c = q.popleft()
            for dx, dy in directions:
                newX = x + dx
                newY = y + dy
                if inBound(grid, newX, newY) and (newX, newY) not in visited:
                    if grid[newX][newY] == '#' and (newX, newY) not in visitedG:
                        ans = ans + c + 1
                    visited.add((newX, newY))
                    if newX in rows or newY in cols:
                        q.append([newX, newY, c + 1000000])
                    else:
                        q.append([newX, newY, c + 1])
    return ans
def inBound(grid, i, j):
    return i >= 0 and j >=0 and i < len(grid) and j < len(grid[0])
def main():
    grid = []
    with open('day11.txt', 'r') as file:
        for line in file:
            grid.append([c for c in line.strip()])
    rows, cols = expand_glaxsy(grid)
    ans = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                visited.add((i, j))
                ans += bfs(grid, [i, j], visited, rows, cols)
    print(ans)

if __name__ == '__main__':
    main()
