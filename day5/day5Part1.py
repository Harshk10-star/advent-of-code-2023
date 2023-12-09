def get_mapped_value(seed, data):
    for d in data:
        source_start, dest_start, length = d
        if dest_start <= seed and dest_start + length >= seed:
            cal = seed - dest_start
            return source_start + cal
    return seed
def main():
    dic = {}
    with open('day5.txt', 'r') as file:
        curr = ''
        seeds = []
        steps = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
        for line in file:
            line = line.split()
            if line:
                if line[0] == 'seeds:':
                    seeds = [int(s) for s in line[1:]]
                    continue
                if not line[0][0].isnumeric():
                    curr = line[0]
                    dic[line[0]] = []
                else:
                    dic[curr].append([int(l) for l in line])
        ans = float('inf')
        print(seeds)
        for seed in seeds:
            curr = seed
            for step in steps:
                curr = get_mapped_value(curr, dic[step])
            ans = min(ans, curr)
        print(ans)
if __name__ == '__main__':
    main()