def main():
    left = []
    right = []
    total_difference = 0
    left_visited = []
    right_visited = []

    with open('input.txt', 'r') as file:
        for line in file:
            left.append(int(line[0:5]))
            right.append(int(line[8:].strip()))

    while len(left_visited) < len(left) and len(right_visited) < len(right):
        left_index = check_smallest_num(left, left_visited)
        right_index = check_smallest_num(right, right_visited)
        difference = get_difference(left_index, right_index)
        total_difference += abs(difference)
        left_visited.append(left_index)
        right_visited.append(right_index)
  
    print(total_difference)
    print(left_visited)
    print(right_visited)



def check_smallest_num(side, visited_indices):
    current_min = float('inf')
    min_index = -1
    for index, elem in enumerate(side):
        if index not in visited_indices and elem < current_min:
            current_min = elem
            min_index = index
    
    #print(f"Minimum is {current_min}, at position {min_index}")
    return min_index

def get_difference(left_index, right_index):
    if right_index > left_index:
        difference = right_index - left_index
    else:
        difference = left_index - right_index
    #print(f"Difference is {difference}")
    if difference < 0:
        difference *= -1
    return abs(difference)


if __name__ == '__main__':
    main()