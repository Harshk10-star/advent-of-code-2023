def get_graph_representation(lineArr):
    lineArr = [[char for char in line.strip()] for line in lineArr]
    return lineArr


def is_number_near_gear(graph, i, j):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for x, y in directions:
        if in_bound(graph, i + x, j + y):
            if graph[i + x][j + y] == '*':
                return True, [i + x, j + y]
    return False, [0, 0]


def in_bound(g, i, j):
    return 0 <= i < len(g) and 0 <= j < len(g[0])

def get_sum_of_numbers(graph, i, j, cols, v):
    # go back to start of number
    for k in range(j - 1, -1, -1):
        if graph[i][k].isnumeric():
            j = k
        else:
            break

    runningSum = 0
    for k in range(j, cols):
        if graph[i][k].isnumeric():
            runningSum = 10 * runningSum + int(graph[i][k])
            v.add((i, k))
        else:
            break
    return runningSum


if __name__ == '__main__':
    total = 0
    nearGear = {}
    with open('day3.txt', 'r') as file:
        lines = file.readlines()
        graph = get_graph_representation(lines)
        R = len(graph)
        C = len(graph[0])
        print(graph)
        visited = set()
        for i in range(R):

            for j in range(C):
                if graph[i][j].isnumeric() and (i, j) not in visited:
                    isnear, arr = is_number_near_gear(graph, i, j)
                    if isnear:
                        t = get_sum_of_numbers(graph, i, j, C, visited)
                        if (arr[0], arr[1]) in nearGear:
                            total += nearGear[(arr[0], arr[1])] * t
                        else:
                            nearGear[(arr[0], arr[1])] = t

        print(total)
