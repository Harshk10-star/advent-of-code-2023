

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
        temp = []
        for c in d:
            if c.isnumeric():
                temp.append(int(c))
        nums.append(temp)
    for i in range(len(nums[0])):
        temp = calulate_milliseconds(nums[1][i], nums[0][i])
        if temp > 0:
            cal *= temp

    print(cal)








if __name__ == '__main__':
    main()
