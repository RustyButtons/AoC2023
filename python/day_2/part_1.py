

with open("day_2/input.txt") as file:
    lines = [line.rstrip() for line in file]


def is_too_high(color, number):
    if color == "red" and number > 12:
        return True
    if color == "green" and number > 13:
        return True
    if color == "blue" and number > 14:
        return True
    return False

total_possible = 0
for line in lines:
    gamenumber, fullgame = line.split(":")
    g_number = int(''.join([i for i in gamenumber if i.isdigit()]).strip(' '))
    cube_games = fullgame.split(";")
    for game in cube_games:
        possible = False
        cubes = game.split(",")        
        for hand in cubes:
            color = ''.join([i for i in hand if not i.isdigit()]).strip(' ')
            number = int(''.join([i for i in hand if i.isdigit()]).strip(' '))
            if is_too_high(color, number):
                g_number = 0
                break
            
    total_possible = total_possible + g_number

print(total_possible)

