def main():
    left = []
    right = []
    total_difference = 0
    part2_counter = 0

    with open('input.txt', 'r') as file:
        for line in file:
            left.append(int(line[0:5]))
            right.append(int(line[8:].strip()))

    left.sort()
    right.sort()

    for i in range(len(left)):
        difference = left[i] - right[i]
        total_difference += abs(difference)
        counter = 0
        for elem in right:
            if left[i] == elem:
                counter += 1
        part2_counter += left[i] * counter

    print(f"Part 1 answer: {total_difference}")
    print(f"Part 2 answer: {part2_counter}")


if __name__ == "__main__":
    main()