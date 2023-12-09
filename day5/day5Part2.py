
'''
data - 2d array
increemnet 1th index until we get seed number, then look at ind0 value
'''
def get_mapped_value(seed, data):
    for d in data:
        source_start, dest_start, length = d
        if dest_start <= seed and dest_start + length >= seed:
            cal = seed - dest_start
            return source_start + cal
    return seed

'''
52 50
53 51
54 52

50 51 54
'''

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
        newSeeds = []

        for i in range(0,len(seeds) - 1, 2):
            newSeeds.append([seeds[i], seeds[i + 1]])
        print(newSeeds)
        for start, offset in newSeeds:
            cache = {}
            for i in range(offset):
                newSeed = start + i
                if start + i in cache:
                    continue
                for step in steps:
                    newSeed = get_mapped_value(newSeed, dic[step])
                cache[start + i] = newSeed
                ans = min(ans, newSeed)

        print(ans)





if __name__ == '__main__':
    main()