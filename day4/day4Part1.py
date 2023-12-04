def get_card_count(arr):
    separate_index = arr.index('|')
    count = 0
    value_set = set(arr[separate_index + 1:])
    for i in range(separate_index):
        if arr[i] in value_set:
            if count == 0:
                count = 1
            else:
                count = count * 2
    return count

if __name__ == '__main__':
    cards = []
    total_count = 0
    with open('day4.txt', 'r') as file:
        for line in file:
            cards.append(line.strip().split()[2:])

    for card in cards:
        total_count += get_card_count(card)

    print(total_count)
