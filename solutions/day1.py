def part1():
    sum = 0
    with open("../input/day1.txt") as input:
        for line in input:
            sum += calculate(int(line))
    print(sum)


def part2():
    sum = 0
    with open("../input/day1.txt") as input:
        for line in input:
            fuel = calculate(int(line))
            sum += fuel
            while calculate(fuel) > 0:
                fuel = calculate(fuel)
                sum += fuel
    print(sum)


def calculate(val: int):
    return (val // 3) - 2


if __name__ == "__main__":
    part1()
    part2()
