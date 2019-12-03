def part1():
    with open("../input/day2.txt") as infile:
        data = parse(infile.readline())
        data[1] = 12
        data[2] = 2
        i = 0
        curr = data[i]
        while curr != 99:
            if curr != 1 and curr != 2:
                print("Error! curr = ", curr)
                return
            if curr == 1:
                data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            elif curr == 2:
                data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
            i += 4
            curr = data[i]
        print(data[0])


def part2():
    with open("../input/day2.txt") as infile:
        return


def parse(s: str):
    return [int(x) for x in s.split(',')]


if __name__ == "__main__":
    part1()
    part2()