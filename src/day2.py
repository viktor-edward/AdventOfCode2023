def readFile(fileInput: str) -> list:
    data = []
    with open(fileInput, "r") as f:
        for line in f.readlines():
            splitPerRound = line.replace("\n", "").split(": ")[1].split("; ")
            data.append([x.split(", ") for x in splitPerRound])
    return data


def containsColor(s: str, c: str) -> int:
    return int(s.split(" ")[0]) if s.find(c) >= 0 else 0


def main():
    data = readFile("../resources/day2_input.txt")

    print("Part one: ")
    sumOfAcceptedGames = 0
    for gameId, game in enumerate(data):
        flattenGame = [item for sublist in game for item in sublist]
        if (max(map(lambda x: containsColor(x, "red"), flattenGame)) <= 12
                and max(map(lambda x: containsColor(x, "green"), flattenGame)) <= 13
                and max(map(lambda x: containsColor(x, "blue"), flattenGame)) <= 14):
            sumOfAcceptedGames += gameId + 1
    print(f"The sum of accepted game ids is {sumOfAcceptedGames}. \n")

    print("\nPart two: ")
    sumOfPowerSets = 0
    for gameId, game in enumerate(data):
        flattenGame = [item for sublist in game for item in sublist]
        sumOfPowerSets += (max(map(lambda x: containsColor(x, "red"), flattenGame)) *
                           max(map(lambda x: containsColor(x, "green"), flattenGame)) *
                           max(map(lambda x: containsColor(x, "blue"), flattenGame)))
    print(f"The power sum of the games is {sumOfPowerSets}. \n")


if __name__ == '__main__':
    main()
