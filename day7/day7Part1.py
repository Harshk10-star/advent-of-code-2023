from collections import Counter


def five_of_a_kind(str):
    count = Counter(str)
    N = len(count.keys())
    if N != 1:

        if 'J' not in count:
            return False
        if N == 2:
            return True

    return True

def four_of_a_kind(str):
    count = Counter(str)
    N = len(count.keys())
    isFour = False
    isOne = False
    if len(count.keys()) != 2:
        return False
    for v in count.values():
        if v == 4:
            isFour = True
        elif v == 1:
            isOne = True

    return isFour and isOne


def full_house(str):
    count = Counter(str)
    isThree = False
    isTwo = False
    if len(count.keys()) != 2:
        return False
    for v in count.values():
        if v == 3 or (v == 2 and 'J' in count):
            isThree = True
        elif v == 2 or (v == 1 and 'J' in count):
            isTwo = True
    return isThree and isTwo

def three_of_a_kind(str):
    count = Counter(str)
    isThree = False
    isOne = False
    if len(count.keys()) != 3:
        return False
    for v in count.values():
        if v == 3 or (v == 2 and 'J' in count):
            isThree = True
        elif v == 1:
            isOne = True
    return isThree and isOne

def two_pair(str):
    count = Counter(str)
    isTwo = 0
    if len(count.keys()) != 3:
        return False
    for v in count.values():
        if v == 2 or (v == 1 and 'J' in count):
            isTwo += 1
    return isTwo == 2

def one_pair(str):
    count = Counter(str)
    isTwo = False
    if len(count.keys()) != 4:
        return False
    for v in count.values():
        if v == 2 or (v == 1 and 'J' in count):
            isTwo = True
    return isTwo


def high_card(str):
    count = Counter(str)
    if len(count.keys()) != 5:
        return False
    return True


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            compare = compare_hands(arr[j][0], arr[j + 1][0])
            if compare == 0:
                compare = tie_breaker(arr[j][0], arr[j + 1][0])
            if compare > 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def tie_breaker(hand1, hand2):
    for i in range(len(hand1)):
        if hand1[i] == hand2[i]:
            continue
        if card_rank(hand1[i]) > card_rank(hand2[i]):
            return 1
        return -1
    return 0


def card_rank(card):
    if card == 'A':
        return 12
    elif card == 'K':
        return 11
    elif card == 'Q':
        return 10
    elif card == 'J':
        return 9
    elif card == 'T':
        return 8
    elif card == '9':
        return 7
    elif card == '8':
        return 6
    elif card == '7':
        return 5
    elif card == '6':
        return 4
    elif card == '5':
        return 3
    elif card == '4':
        return 2
    elif card == '3':
        return 1
    else:
        return 0


def hand_rank(hand):
    if five_of_a_kind(hand):
        return 7
    elif four_of_a_kind(hand):
        return 6
    elif full_house(hand):
        return 5
    elif three_of_a_kind(hand):
        return 4
    elif two_pair(hand):
        return 3
    elif one_pair(hand):
        return 2
    elif high_card(hand):
        return 1
    else:
        return 0



def compare_hands(hand1, hand2):
    rank1 = hand_rank(hand1)
    rank2 = hand_rank(hand2)
    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return -1
    else:
        return 0


def cal_bidding(arr):
    ans = 0
    rank = 1
    for i in range(len(arr)):
        ans += rank * arr[i][1]
        rank += 1
    return ans


def main():
    cards = []
    with open('day7.txt', 'r') as file:
        for line in file:
            card, bid = line.strip().split(' ')
            cards.append([card, int(bid)])

    bubble_sort(cards)
    print(cal_bidding(cards))


if __name__ == '__main__':
    main()
