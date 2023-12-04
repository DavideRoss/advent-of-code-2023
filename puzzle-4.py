import re
import functools

lines = [x.strip() for x in open('data-4.txt', 'r').readlines()]

# Part 1
sum = 0
for line in lines:
    data = re.match(r'Card[ ]+\d+: ([^|]+) \| (([^|]+))$', line)
    winning = [int(x) for x in data.group(1).split(' ') if x]
    card = [int(x) for x in data.group(2).split(' ') if x]
    exp = functools.reduce(lambda acc, el: int(el in winning) + acc, card, 0)

    if exp > 0:
        sum += pow(2, exp - 1)

print(f'Part 1 sum: {sum}')

# Part 2
sum = 0
cards = {}

for i in range(len(lines)):
    cards[i + 1] = 1

for card in cards:
    data = re.match(r'Card[ ]+\d+: ([^|]+) \| (([^|]+))$', lines[card - 1])
    winning = [int(x) for x in data.group(1).split(' ') if x]
    curr = [int(x) for x in data.group(2).split(' ') if x]
    win = functools.reduce(lambda acc, el: int(el in winning) + acc, curr, 0)
    sum += cards[card]
    for i in range(card + 1, card + win + 1):
        cards[i] += cards[card]

print(f'Part 2 sum: {sum}')
    