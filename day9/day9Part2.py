
def check_all_zeros(arr):
    for i in range(len(arr)):
        if arr[i] != 0:
            return False
    return True
def get_extrapolate_count(start):
    lvl = {}
    rank = 1
    lvl[rank] = [n for n in start]
    while True:
        rank += 1
        temp = []
        for i in range(len(start) - 1):
            temp.append(start[i + 1] - start[i])
        lvl[rank] = temp
        start = [n for n in temp]
        if check_all_zeros(temp):
            break
    # extrapolate time
    print(lvl)
    for i in range(rank - 1, 0, -1):
        lvl[i].insert(0,lvl[i][0] - lvl[i + 1][0])
    return lvl[1][0]
def main():
    count = 0
    with open('day9.txt', 'r') as file:

        for line in file:
            arr = [int(n) for n in line.strip().split(' ')]
            count += get_extrapolate_count(arr)

    print(count)

if __name__ == '__main__':
    main()