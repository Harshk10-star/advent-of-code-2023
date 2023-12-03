def get_combined_number(line):
    left = get_first_half(line)
    right = get_second_half(line)
    return int(left + right)


def get_first_half(line):
    for i in range(len(line)):
        if line[i].isnumeric():
            return line[i]
    return ''


def get_second_half(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isnumeric():
            return line[i]
    return ''


def main():
    ans = []
    with open('day1.txt', 'r') as file:
        for line in file:
            line = line.strip()
            combinedNumber = get_combined_number(line)
            ans.append(combinedNumber)

    print(sum(ans))


if __name__ == '__main__':
    main()
