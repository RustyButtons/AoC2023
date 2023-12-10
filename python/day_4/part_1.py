# with open("day_4/test.txt") as file:
with open("day_4/input.txt") as file:
    lines = [line.rstrip() for line in file]


def get_points(matches: int) -> int:
    # initialization
    count = 1
    # exit limit
    points = 1
    while count in range(matches):
        count += 1
        points = points * 2
    print("points: ", points)
    return points


def check_matches(winners: list, yours: list) -> int:
    matches = 0
    for i in winners:
        for j in yours:
            if j == i:
                print("match: ", i, " & ", j)
                matches = matches + 1
    return matches


winner_winner_chicken_dinner = 0
for line in lines:
    gamenumber, fullgame = line.split(":")
    print(gamenumber)
    print(fullgame)
    winners, yours = fullgame.split("|")
    winners = list(map(int, winners.split()))
    yours = list(map(int, yours.split()))
    matches = check_matches(winners, yours)
    # matches = len(set(winners) & set(yours))
    if matches == 1:
        print("Total matches: ", str(matches))
        winner_winner_chicken_dinner = winner_winner_chicken_dinner + 1
    elif matches > 1:
        print("Total matches: ", str(matches))
        winner_winner_chicken_dinner = winner_winner_chicken_dinner + get_points(
            matches
        )


print(winner_winner_chicken_dinner)
