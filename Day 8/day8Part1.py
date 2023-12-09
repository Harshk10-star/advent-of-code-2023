from collections import defaultdict
def get_graph_representation(arr):
    adj = defaultdict(list)
    for dir in arr:
        dir = dir.replace('=', '').replace('(', '').replace(')', '').replace(',', '').strip().split(' ')
        adj[dir[0]].append(dir[2])
        adj[dir[0]].append(dir[3])
    return adj
def count_steps(pattern, graph, i, curr, count):
    while True:
        if curr == 'ZZZ':
            return count
        if i >= len(pattern):
            i = 0
        if pattern[i] == 'L':
            curr = graph[curr][0]
            count += 1
        else:
            curr = graph[curr][1]
            count += 1
        i += 1
def main():
    with open('day8.txt', 'r') as file:
        lines = []
        moves = ''
        for line in file:
            lines.append(line.strip())
        print(lines)
        i = 0
        while lines[i] != '':
            moves += lines[i]
            i += 1
        lines = lines[i + 1:]
        print(lines)
        graph = get_graph_representation(lines)
        ans = count_steps(moves, graph, 0, 'AAA', 0)
        print(ans)

if __name__ == '__main__':
    main()