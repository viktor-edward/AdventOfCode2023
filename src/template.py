def readFile(fileInput: str) -> list:
    data = []
    with open(fileInput, "r") as f:
        for line in f.readlines():
            data.append(int(line.replace("\n", "")))
    return data


def main():
    data = readFile("../resources/day1_input.txt")

    print("Part one: ")

    print("\nPart two: ")


if __name__ == '__main__':
    main()
