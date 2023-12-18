from collections import deque
def search(arr, connections, startX, startY, N, M):
    directions = [[-1, 0, 'N'], [1, 0, 'S'], [0, -1, 'W'], [0, 1, 'E']]
    q = deque()
    q.append([startX, startY])
    visited = set()
    visited.add((startX, startY))
    steps = []
    count = 1
    while q:
        count += 1
        x, y = q.popleft()
        if arr[x][y] == 'S':

            visited.add((x,y))

            break
        pipe = connections[arr[x][y]]
        for dx, dy, dir in directions:
            if dir in pipe:
                newX, newY = x + dx, y + dy
                if in_bound(newX, newY, N, M) and arr[newX][newY] != '.' and (newX, newY) not in visited:
                    if arr[newX][newY] == 'S':
                        steps.append((newX, newY))
                        continue
                    dir1, dir2 = connections[arr[newX][newY]]
                    if dir1 == opposite(dir) or dir2 == opposite(dir):

                        q.append([newX, newY])
                        visited.add((newX, newY))
                        steps.append((newX, newY))
                    else:
                        return 0
    return count // 2, steps
def count_enclosed_tiles(loop, grid, connections):
    q = deque()
    N = len(grid)
    M = len(grid[0])
    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.':
                q.append([i, j])
    while q:
        #check all four directions
        x, y = q.popleft()

        isValid = False
        #check up
        for i in range(x - 1, -1, -1):
            if grid[i][y] in connections:

                if (i, y) in loop:
                    isValid = True
        if not isValid:
            continue
        isValid = False
        #check down
        for i in range(x + 1, N, 1):
            if grid[i][y] in connections:
                if (i, y) in loop:
                    isValid = True
        if not isValid:
            continue
        isValid = False

        #check right
        for i in range(y + 1, M, 1):
            if grid[x][i] in connections:
                if (x, i) in loop:
                    isValid = True
        if not isValid:
            continue
        isValid = False
        #check left
        for i in range(y - 1, -1, -1):
            if grid[x][i] in connections:
                if (x, i) in loop:
                    isValid = True
        if not isValid:
            continue
        count += 1
    return count

def opposite(dir):
    dic = {
        'N': 'S',
        'S': 'N',
        'W': 'E',
        'E': 'W',
    }
    return dic[dir]
def in_bound(x, y, N, M):
    return x >= 0 and y >= 0 and x < N and y < M
def main():
    connections = {
        '|': ['N', 'S'],
        '-': ['E', 'W'],
        'L': ['N', 'E'],
        'J': ['N', 'W'],
        '7': ['S', 'W'],
        'F': ['S', 'E'],
    }
    arr = []
    with open('day10.txt', 'r') as file:
        for line in file:
            arr.append([n for n in line.strip()])

    directions = [[-1,  0], [1, 0], [0, 1], [0, -1]]
    N = len(arr)
    M = len(arr[0])
    ans = 0
    results = []

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'S':

                for dx, dy in directions:
                    newX = i + dx
                    newY = j + dy
                    if in_bound(newX, newY, N, M):
                        if arr[newX][newY] == '.':
                            continue
                        count, steps = search(arr, connections, newX, newY, N, M)
                        if ans < count:
                            ans = count
                            results = steps
    print(results)
    ans = count_enclosed_tiles(results, arr, connections)
    print(ans)
if __name__ == '__main__':
    main()