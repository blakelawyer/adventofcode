file = open("input.txt", "r")
lines = [line.strip() for line in file]

total = 0
for line in lines:
    digits = ""
    for c in line:
        if c.isdigit():
            digits = digits + c
    if digits != 0:
        total += int(digits[0] + digits[-1])
print(f"Part 1: {total}")

def digitize(line, numbers):
    for i, num in enumerate(numbers):
        line = line.replace(num, num[0] + str(i+1) + num[-1])
    return line

total = 0
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in lines:
    line = digitize(line, numbers)
    digits = ""
    for c in line:
        if c.isdigit():
            digits = digits + c
    if digits != 0:
        combination = int(digits[0] + digits[-1])
        total += combination 
print(f"Part 2: {total}")

