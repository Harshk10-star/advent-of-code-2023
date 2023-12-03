def is_good_set(i, j, line):
    endOfGame = False
    while not endOfGame and i < j:
        num = int(line[i])

        colr = line[i + 1]
        if colr[-1] == ';':
            endOfGame = True
            colr = colr[0: -1]
        if colr[-1] == ',':
            colr = colr[0: -1]
        if num > cubes[colr]:
            return False, -1
        i += 2
    return True, i


if __name__ == '__main__':
    cubes = {
        'green': 13,
        'blue': 14,
        'red': 12
    }
    total = 0
    with open('day2.txt', 'r') as file:
        # Read each line
        for line in file:
            line = line.strip().split(' ')
            game_id = int(line[1][:-1])
            i = 2
            j = len(line) - 1
            addToSum = True
            while i < j:
                isGood, start = is_good_set(i, j, line)
                if not isGood:
                    addToSum = False
                    break
                i = start
            if addToSum:
                total += game_id
        print(total)
