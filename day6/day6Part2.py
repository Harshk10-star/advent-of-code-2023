

def calulate_milliseconds(distance, time):
    number_of_wins = 0

    for i in range(time):
        cal = (time - i) * i
        if cal > distance:
            number_of_wins += 1
    return  number_of_wins

def main():
    ans = []
    with open('day6.txt', 'r') as file:
        for line in file:
            ans.append(line.strip().split(' '))
    nums = []
    cal = 1
    for d in ans:
        temp = ''
        for c in d:
            if c.isnumeric():
                temp += c
        if temp != '':
            nums.append(int(temp))

    print(calulate_milliseconds(nums[1], nums[0]))








if __name__ == '__main__':
    main()
