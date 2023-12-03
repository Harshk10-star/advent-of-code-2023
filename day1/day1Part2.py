def get_combined_number(line, nums, loop):

    first = get_first_half(line, nums, loop)
    second = get_second_half(line, nums, loop)
    return int(first + second)


def get_first_half(line, nums, loop):
    for i in range(len(line)):
        if line[i].isnumeric():
            return line[i]
        for v in loop:
            if i + v - 1 < len(line) and line[i: i + v] in nums:
                return str(nums[line[i: i + v]])
    return ''


def get_second_half(line, nums, loop):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isnumeric():
            return line[i]
        for v in loop:
            if i - (v - 1) >= 0 and line[i - (v - 1): i + 1] in nums:
                return str(nums[line[i - (v - 1): i + 1]])
    return ''


def main():
    nums = {
        "one": 1,
        'two': 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    loop = [3, 5, 4]
    ans = []
    with open('day1.txt', 'r') as file:
        for line in file:
            line = line.strip()
            combinedNumber = get_combined_number(line, nums, loop)
            ans.append(combinedNumber)

    print(sum(ans))


if __name__ == '__main__':
    main()
