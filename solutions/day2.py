def calculate(data: []):
    i = 0
    curr = data[i]
    while curr != 99:
        if curr != 1 and curr != 2:
            print("Error! curr = ", curr)
            return
        if curr == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
        elif curr == 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
        i += 4
        curr = data[i]
    return data[0]


def part1():
    with open("../input/day2.txt") as infile:
        data = parse(infile.readline())
        data[1] = 12
        data[2] = 2
        result = calculate(data)
        print(result)


def part2():
    with open("../input/day2.txt") as infile:
        _data = parse(infile.readline())
        for i in range(0, 100):
            for j in range(0, 100):
                data = _data.copy()
                data[1] = i
                data[2] = j
                result = calculate(data)
                if result == 19690720:
                    print(100 * i + j)
                    return


def parse(s: str):
    return [int(x) for x in s.split(',')]


if __name__ == "__main__":
    part1()
    part2()