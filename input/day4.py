import re


def check(password: int):
    dubs = False
    prev = 10
    x = password % 10
    count = 0
    while x > 0:
        if x > prev:
            return False
        if x == prev:
            dubs = True
        password = password // 10
        prev = x
        x = password % 10
        count += 1
    return dubs and count == 6


def check2(password: int):
    digs = [int(d) for d in str(password)]
    difs = [digs[i] - digs[i + 1] for i in range(len(digs)-1)]
    if any([x > 0 for x in difs]):
        return False
    stringified = ''.join([str(x) for x in difs])
    stringified = re.sub(r"0{2,}", '', stringified)
    return stringified.__contains__("0")


def part1():
    with open("../input/day4.txt") as infile:
        nums = [int(x) for x in infile.readline().split("-")]
    print(len([x for x in range(nums[0], nums[1]) if check(x)]))


def part2():
    with open("../input/day4.txt") as infile:
        nums = [int(x) for x in infile.readline().split("-")]
    print(len([x for x in range(nums[0], nums[1]) if check2(x)]))


if __name__ == "__main__":
    part1()
    part2()
