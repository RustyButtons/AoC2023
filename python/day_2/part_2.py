with open("day_2/input.txt") as file:
    lines = [line.rstrip() for line in file]

total_power = 0
for line in lines:
    gamenumber, fullgame = line.split(":")
    cube_games = fullgame.split(";")
    power = 1
    red = 0
    green = 0
    blue = 0
    for game in cube_games:
        cubes = game.split(",")
        for hand in cubes:
            color = ''.join([i for i in hand if not i.isdigit()]).strip(' ')
            number = int(''.join([i for i in hand if i.isdigit()]).strip(' '))
            if color == "red":
                red = max(number, red)
            if color == "green":
                green = max(number, green)
            if color == "blue":
                blue = max(number, blue)

        numbers = [red, green, blue]
        numbers = [i for i in numbers if i != 0]
        power = 1
        for num in numbers:
            power *= num
    total_power = total_power + power

print(total_power)
