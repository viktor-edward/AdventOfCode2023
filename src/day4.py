import math


def readFile(fileInput: str) -> list:
    winningNumbers, myNumbers = [], []
    with open(fileInput, "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "").replace("  ", " ").split(": ")[1].split(" | ")
            winningNumbers.append(set(line[0].split(" ")))
            myNumbers.append(set(line[1]. split(" ")))
    return winningNumbers, myNumbers


def main():
    winningNumbers, myNumbers = readFile("../resources/day4_input.txt")
    numberOfGames = len(winningNumbers)

    print("Part one: ")
    matchingNumbers = map(lambda x, y: len(x.intersection(y)), winningNumbers, myNumbers)
    totalPoints = sum(map(lambda x: math.pow(2, x - 1) if x > 0 else 0, matchingNumbers))
    print(f"The total points of the tickets is {totalPoints}. \n")

    print("\nPart two: ")
    tickets = [1] * numberOfGames
    matchingNumbers = map(lambda x, y: len(x.intersection(y)), winningNumbers, myNumbers)
    for i, points in enumerate(matchingNumbers):
        for j in range(points):
            if j >= numberOfGames:
                break
            else:
                tickets[i + j + 1] += tickets[i]
    print(f"The total amount of tickets is {sum(tickets)}. \n")


if __name__ == '__main__':
    main()
