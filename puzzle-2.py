import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

MAX_VAL = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('data-2.txt', 'r') as file:
    lines = file.readlines()

# Part 1
def test_pulls(data):
    for pull in data:
        for col in pull.split(', '):
            parts = re.findall(r'(\d+) (red|green|blue)', col)[0]
            if int(parts[0]) > MAX_VAL[parts[1]]:
                return False

    return True

sum = 0
for line in lines:
    parts = re.findall(r'Game (\d+): (.*)', line)[0]
    if test_pulls(parts[1].split('; ')):
        sum += int(parts[0])

print('Part 1 sum: ' + str(sum))

# Part 2
sum = 0
for line in lines:
    parts = re.findall(r'Game (\d+): (.*)', line)[0]
    curr_min = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for i, pull in enumerate(parts[1].split('; ')):
        for col in pull.split(', '):
            cubes = re.findall(r'(\d+) (red|green|blue)', col)[0]
            if (int(cubes[0]) > curr_min[cubes[1]]):
                curr_min[cubes[1]] = int(cubes[0])

    sum += curr_min['red'] * curr_min['green'] * curr_min['blue']

print('Part 2 sum: ' + str(sum))
                