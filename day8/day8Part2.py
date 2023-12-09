import math
from collections import defaultdict
def get_graph_representation(arr):
    adj = defaultdict(list)
    nodes = []
    for dir in arr:
        dir = dir.replace('=', '').replace('(', '').replace(')', '').replace(',', '').strip().split(' ')
        nodes.append(dir[0])
        adj[dir[0]].append(dir[2])
        adj[dir[0]].append(dir[3])
    return adj, nodes
def count_steps(pattern, graph, i, curr, count):
    while True:
        if curr[2] == 'Z':
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
        pattern = ''
        for line in file:
            lines.append(line.strip())
        i = 0
        while lines[i] != '':
            pattern += lines[i]
            i += 1
        lines = lines[i + 1:]
        graph, nodes = get_graph_representation(lines)
        starting_nodes = []
        for node in nodes:
            if node[2] == 'A':
                starting_nodes.append(node)
        sums = []
        for node in starting_nodes:
            sums.append(count_steps(pattern, graph, 0, node, 0))
        print(math.lcm(*sums))
if __name__ == '__main__':
    main()