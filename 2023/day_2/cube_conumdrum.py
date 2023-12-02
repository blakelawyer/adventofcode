file = open("input.txt", "r")
lines = [line.strip() for line in file]

possible_red = 12
possible_green = 13
possible_blue = 14
total = 0
for line in lines:
    valid = True
    line = line.split(':')
    game = [int(s) for s in line[0].split() if s.isdigit()][0]
    sets = line[1].split(';')
    for set in sets:
        cubes = set.split(',')
        for cube in cubes:
            count = [int(s) for s in cube.split() if s.isdigit()][0]
            color = [s for s in cube.split() if not s.isdigit()][0]
            if color == 'red':
                if count > possible_red:
                    valid = False
            elif color == 'blue':
                if count > possible_blue:
                    valid = False
            elif color == 'green':
                if count > possible_green:
                    valid = False
    if valid:
        total += game
print(f"Part 1: {total}")

total = 0
for line in lines:
    min_red = 0; min_blue = 0; min_green = 0
    line = line.split(':')
    game = [int(s) for s in line[0].split() if s.isdigit()][0]
    sets = line[1].split(';')
    for set in sets:
        cubes = set.split(',')
        for cube in cubes:
            count = [int(s) for s in cube.split() if s.isdigit()][0]
            color = [s for s in cube.split() if not s.isdigit()][0]
            if color == 'red':
                if count > min_red:
                    min_red = count
            elif color == 'blue':
                if count > min_blue:
                    min_blue = count
            elif color == 'green':
                if count > min_green:
                    min_green = count
    power = min_red * min_blue * min_green
    total += power
    print(f"Part 2: {total}")






            
        


