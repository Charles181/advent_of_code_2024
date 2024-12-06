import re

def main():
    with open('input.txt') as file:
        lines = file.read().strip()
    regex = r"mul\(\d+,\d+\)"
    m = re.findall(regex, lines)
    # print(m)
    result = 0

    for mul in m:
        nums = re.findall(r'\d+', mul)
        result += int(nums[0]) * int(nums[1])
    
    print(f"Part 1 answer: {result}")

    enabled = True
    result2 = 0
    state_r = r"do\(\)|don't\(\)"
    states = re.findall(f"{state_r}|{regex}", lines)

    for state in states:
        if state == "do()":
            enabled = True
        if state == "don't()":
            enabled = False
        if enabled and state.startswith("mul"):
            nums = re.findall(r'\d+', state)
            result2 += int(nums[0]) * int(nums[1])
    
    print(f"Part 2 answer: {result2}")
    

if __name__ == '__main__':
    main()