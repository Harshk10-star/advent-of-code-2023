def get_graph_representation(lineArr):
    lineArr = [[char for char in line.strip()] for line in lineArr]
    return lineArr


def is_number_near_symbol(graph, i , j):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for x, y in directions:
        if in_bound(graph, i + x, j + y):
            if is_symbol(graph[i + x][j + y]):
                return True
    return False


def in_bound(g, i, j):
    return 0 <= i < len(g) and 0 <= j < len(g[0])

def is_symbol(char):
    symbols = "!@#$%^&*()_-+={}[]|\\:;\"'<>,?/~`"
    return char in symbols


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
    with open('day3.txt', 'r') as file:
        lines = file.readlines()
        graph = get_graph_representation(lines)
        R = len(graph)
        C = len(graph[0])
        visited = set()
        for i in range(R):

            for j in range(C):
                if graph[i][j].isnumeric() and (i, j) not in visited:

                    if is_number_near_symbol(graph, i, j):
                        t = get_sum_of_numbers(graph, i, j, C, visited)
                        total += t

        print(total)