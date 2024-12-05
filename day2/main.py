def main():
    file = open('input.txt').read().strip()
    # print(file)
    levels = file.split('\n')
    # print(levels)
    counter = 0
    for level in levels:
        lvl = list(map(int, level.split()))
        safe_counter = 0
        for i in range(len(lvl)-1):
            safe = True
            if i > 0:
                if (lvl[i-1] < lvl[i] and lvl[i] > lvl[i+1]) or (lvl[i-1] > lvl[i] and lvl[i] < lvl[i+1]):
                    continue
            difference = abs(lvl[i] - lvl[i+1])
            # print(difference)
            if difference == 0 or difference > 3:
                safe = False
            if safe:
                safe_counter +=1
        if safe_counter == len(lvl)-1:
            counter += 1
        print(f"**{safe_counter}**")
        print("-----")
        
    print(counter)

if __name__ == '__main__':
    main()