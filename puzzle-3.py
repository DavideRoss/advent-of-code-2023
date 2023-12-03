import re

lines = [x.strip() for x in open('data-3.txt', 'r').readlines()]

# Part 1
def check_valid(start, end, li):
    for y in range(max(li - 1, 0), min(li + 2, len(lines))):
        for x in range(max(start - 1, 0), min(end + 1, len(lines[0]) - 1) + 1):
            if re.match(r'(?![\d\.])', lines[y][x]):
                return True
    return False

sum = 0
for i, line in enumerate(lines):
    for n in re.finditer(r'(\d+)', line):
        test = check_valid(n.span()[0], n.span()[1] - 1, i)
        if test:
            sum += int(n.group(0))

print(f'Part 1 sum: {sum}')

# Part 2
def check_neighbors(i, li):
    nums = []
    y_min, y_max = max(li - 1, 0), min(li + 2, len(lines))
    x_min, x_max = max(i - 1, 0), min(i + 1, len(lines[0]) - 1) + 1

    for y in range(y_min, y_max):
        for n in re.finditer(r'\d+', lines[y]):
            span = n.span()
            if x_min <= span[0] < x_max or x_min < span[1] <= x_max:
                nums.append(int(n.group(0)))

    if len(nums) == 2:
        return nums[0] * nums[1]
    else:
        return 0

sum = 0
for i, line in enumerate(lines):
    for n in re.finditer(r'\*', line):
        sum += check_neighbors(n.span()[0], i)

print(f'Part 2 sum: {sum}')