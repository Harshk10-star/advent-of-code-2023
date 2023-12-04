from collections import deque
from collections import defaultdict

def count_matching_numbers(card):
    separator_index = card.index('|')
    count = 0
    winning_numbers = set(card[separator_index + 1:])
    for i in range(separator_index):
        if card[i] in winning_numbers:
            count += 1
    return count

if __name__ == '__main__':
    cards = []
    card_counts = defaultdict(int)
    with open('day4.txt', 'r') as file:
        for line in file:
            cards.append(line.strip().split()[2:])
    N = len(cards)
    matching_counts = [count_matching_numbers(card) for card in cards]

    card_queue = deque(range(1, len(matching_counts) + 1))
    while card_queue:
        current_card = card_queue.popleft()

        card_counts[current_card] += 1
        if current_card - 1 >= len(matching_counts):
            continue
        for v in range(1, matching_counts[current_card - 1] + 1):
            card_queue.append(current_card + v)

    total_cards = sum(card_counts.values())
    print(total_cards)
