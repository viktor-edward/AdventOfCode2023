def readFile(fileInput):
    data = []
    with open(fileInput, "r") as file:
        for line in file.readlines():
            data.append((line.replace("\n", "")))
    return data


def getNumberPart1(text: str) -> int:
    first, last = -1, 0
    for s in text:
        if s.isdigit():
            last = int(s)
            if first < 0:
                first = int(s)
    return first*10 + last


def getNumberPart2(text: str) -> int:
    matchingCriterias = (["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
                         + list((str(x) for x in range(1, 10))))
    firstValue, firstPos, lastValue, lastPos = 0, 999999, 0, 0
    for count, criteria in enumerate(matchingCriterias):
        first, last = text.find(criteria), text.rfind(criteria)
        if -1 < first <= firstPos:
            firstPos = first
            if criteria.isdigit():
                firstValue = 10 * int(criteria)
            else:
                firstValue = 10 * (count + 1)
        if last >= lastPos:
            lastPos = last
            if criteria.isdigit():
                lastValue = int(criteria)
            else:
                lastValue = count + 1
    return firstValue + lastValue


def main():
    data = readFile("../resources/day1_input.txt")

    print("Part one: ")
    totalCalibration = sum(getNumberPart1(x) for x in data)
    print(f"The total calibration value is {totalCalibration}. \n")


    print("Part two: ")
    totalCalibrationPart2 = sum(getNumberPart2(x) for x in data)
    print(f"The total calibration value is {totalCalibrationPart2}. \n")


if __name__ == '__main__':
    main()
