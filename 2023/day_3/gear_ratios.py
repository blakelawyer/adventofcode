file = open("input.txt", "r")
lines = [line.strip() for line in file]

part_found = False
part_number = ''
sum = 0
gears = {}
current_gears = []
ratio = 0
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for i, line in enumerate(lines):
    print(lines[i])
    for j, character in enumerate(line):
        if lines[i][j].isdigit():
            part_number = part_number + lines[i][j]
            for direction in directions:
                y, x = direction
                try:
                    if not lines[i + y][j + x].isalnum() and lines[i + y][j + x] != '.' and i + y >= 0:
                        if lines[i + y][j + x] == '*':
                            if [i + y, j + x] not in current_gears:
                                current_gears.append([i + y, j + x])
                        part_found = True
                except:
                    pass
        else:
            if part_found:
                sum += int(part_number)
                part_found = False
                if current_gears:
                    for gear in current_gears:
                        if str(gear) in gears:
                            gears[str(gear)].append(int(part_number))
                        else:
                            gears[str(gear)] = [int(part_number)]
            part_number = ''
            current_gears = []
            
for gear in gears.values():
    if len(gear) == 2:
        ratio += gear[0] * gear[1]
        
print(f"Part 1: {sum}")
print(f"Part 2: {ratio}")
