# Part 1
file = open("./trebuchet.txt", "r")
lines = [line.strip() for line in file]

total = 0
for line in lines:
    digits = ""
    for c in line:
        if c.isdigit():
            digits = digits + c
    if digits != 0:
        total += int(digits[0] + digits[-1])
