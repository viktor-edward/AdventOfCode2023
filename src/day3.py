def readFile(fileInput: str) -> list:
    data = []
    with open(fileInput, "r") as f:
        for line in f.readlines():
            data.append(line.replace("\n", ""))
    return data


class schematicNumber:
    def __init__(self, number: int, startPos: tuple, endPos: tuple):
        self.number = number
        self.startPos = startPos
        self.endPos = endPos

    def __str__(self):
        return f"Number {str(self.number)} starting at {str(self.startPos)} ending at {str(self.endPos)}."


class specialSymbol:
    def __init__(self, symbol: str, pos: tuple):
        self.symbol = symbol
        self.pos = pos

    def __str__(self):
        return str(self.pos)


def isSpecialCharacterTouchingNumber(sn: schematicNumber, sym: specialSymbol):
    if (sn.startPos[1] - 1) <= sym.pos[1] <= (sn.endPos[1] + 1) and abs(sn.startPos[0] - sym.pos[0]) <= 1:
        return True
    else:
        return False


def gearValue(snList: list, sym: specialSymbol):
    oneHit = False
    firstValue = 0
    for sn in snList:
        if isSpecialCharacterTouchingNumber(sn, sym):
            if oneHit:
                return firstValue * sn.number
            else:
                oneHit = True
                firstValue = sn.number

    return 0


def main():
    data = readFile("../resources/day3_input.txt")

    print("Part one: ")
    # Collect all number and special characters together with their positions
    foundNumbers, foundSpecialSymbols = [], []
    tempDigit = ""
    newDigit = False
    maxWidth, maxHeight = len(data[0]),  len(data)
    tempStart, tempEnd = 0, 0
    for i in range(maxHeight):
        for j in range(maxWidth):
            if data[i][j].isdigit():
                if not newDigit:
                    tempDigit = data[i][j]
                    newDigit = True
                    tempStart = (i, j)
                    tempEnd = (i, j)
                else:
                    tempDigit += data[i][j]
                    tempEnd = (i, j)
            elif data[i][j] != ".":
                foundSpecialSymbols.append(specialSymbol(data[i][j], (i, j)))

            if (not data[i][j].isdigit() or j == maxWidth - 1) and newDigit:
                newDigit = False
                foundNumbers.append(schematicNumber(int(tempDigit), tempStart, tempEnd))
                tempDigit = ""

    # For each number see if any special symbol is touching it, if so add it to the total sum
    totSum = 0
    for sn in foundNumbers:
        for sym in foundSpecialSymbols:
            if isSpecialCharacterTouchingNumber(sn, sym):
                totSum += sn.number
                break
    print(f"The sum the of accepted numbers is {totSum}. \n")

    print("\nPart two: ")
    # Loop over foundSpecialSymbols and check all the ones a that are "*" if they have two adjacent numbers
    totSumGears = sum(map(lambda x: gearValue(foundNumbers, x),
                          filter(lambda s: s.symbol == "*", foundSpecialSymbols)))
    print(f"The sum the of accepted gears is {totSumGears}. \n")


if __name__ == '__main__':
    main()
