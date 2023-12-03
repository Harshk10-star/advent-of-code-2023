def get_combined_number(line):
    combinedNumber = ''
    combinedNumber = get_first_half(line, combinedNumber)
    combinedNumber = get_second_half(line, combinedNumber)
    return int(combinedNumber)


def get_first_half(line, combinedNumber):
    for i in range(len(line)):
        if line[i].isnumeric():
            combinedNumber = line[i] + combinedNumber
            break
    return combinedNumber


def get_second_half(line, combinedNumber):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isnumeric():
            combinedNumber = combinedNumber + line[i]
            break
    return combinedNumber


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
