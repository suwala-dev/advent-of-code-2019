def draw(line: [], distances: {} = None) -> set:
    s = set()
    x, y = 0, 0
    steps = 0
    for instruction in line:
        dx, dy = 0, 0
        direction = instruction[0]
        if direction == "R":
            dx, dy = 1, 0
        elif direction == "L":
            dx, dy = -1, 0
        elif direction == "U":
            dx, dy = 0, 1
        elif direction == "D":
            dx, dy = 0, -1
        else:
            exit("Unsupported direction " + direction)
        for i in range(0, int(instruction[1:])):
            steps += 1
            x += dx
            y += dy
            s.add((x, y))
            if distances is not None and (x, y) not in distances:
                distances[(x, y)] = steps
    return s


def part1():
    lines = []
    with open("../input/day3.txt") as infile:
        for line in infile:
            lines.append(line.split(","))
    paths = []
    for line in lines:
        paths.append(draw(line))
    print(min(abs(x) + abs(y) for x, y in paths[0].intersection(paths[1])))


def part2():
    lines = []
    with open("../input/day3.txt") as infile:
        for line in infile:
            lines.append(line.split(","))
    d1 = {}
    d2 = {}
    one = draw(lines[0], d1)
    two = draw(lines[1], d2)
    print(min(d1[(x, y)] + d2[(x, y)] for x, y in one.intersection(two)))


if __name__ == "__main__":
    part1()
    part2()
