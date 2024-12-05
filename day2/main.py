def is_safe(levels):
    for i in range(len(levels) - 1):
        if abs(levels[i] - levels[i + 1]) > 3 or abs(levels[i] - levels[i + 1]) == 0:
            return False
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    return increasing or decreasing


def main():
    with open('input.txt') as file:
        levels = file.read().strip().split('\n')

    counter = 0
    counter2 = 0
    for level in levels:
        lvl = list(map(int, level.split()))

        if is_safe(lvl):
            counter += 1
            counter2 += 1
            continue

        for i in range(len(lvl)):
            modified_levels = lvl[:i] + lvl[i + 1:]
            if is_safe(modified_levels):
                counter2 += 1
                break
    print(counter)
    print(counter2)


if __name__ == '__main__':
    main()
