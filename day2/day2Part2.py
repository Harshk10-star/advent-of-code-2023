def min_cubes(i, j, line, red, green, blue):
    while i < j:
        num = int(line[i])
        color = line[i + 1].rstrip(';,')
        if color == 'red':
            red = max(red, num)
        elif color == 'blue':
            blue = max(blue, num)
        else:
            green = max(green, num)
        if line[i + 1][-1] == ';':
            i += 2
            break
        i += 2
    return i, red, green, blue


if __name__ == '__main__':
    total_power = 0
    with open('day2.txt', 'r') as file:
        for line in file:
            line = line.strip().split(' ')
            i = 2
            j = len(line) - 1
            min_red = min_blue = min_green = 0
            while i < j:
                start, new_red, new_green, new_blue = min_cubes(i, j, line, min_red, min_green, min_blue)
                min_red, min_blue, min_green = max(min_red, new_red), max(min_blue, new_blue), max(min_green, new_green)
                i = start
            total_power += min_blue * min_green * min_red

        print(total_power)
