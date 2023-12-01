import re

WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def parse_num(x):
    if len(x) > 1:
        return str(WORDS.index(x) + 1)
    return x

with open('data-1.txt', 'r') as file:
    lines = file.readlines()

# Part 1
sum = 0
for line in lines:
    digits = re.findall('\d', line)
    num = int(digits[0] + digits[-1])
    sum += num

print('Part 1 sum: ' + str(sum))

# Part 2
sum = 0
for line in lines:
    line_words = re.findall('(?=(\d|' + '|'.join(WORDS) + '))', line)
    digits = list(map(parse_num, [line_words[0], line_words[-1]]))
    sum += int(digits[0] + digits[-1])

print('Part 2 sum: ' + str(sum))