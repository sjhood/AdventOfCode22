
def part1():
    with open('input.txt') as f:
        sum = 0
        for line in f:
            common_letter = ''
            part1 = line[0:int(len(line)/2)]
            part2 = line[int(len(line)/2)::]

            common_letter = helper(part1, part2)
            if common_letter[0].isupper():
                sum += ord(common_letter[0]) - 38
            else:
                sum += ord(common_letter[0]) - 96
            print(sum)
            # print(part2)

def part2():
    with open('input.txt') as f:
        sum = 0
        current_compare = []
        for line in f:
            if len(current_compare) < 3:
                current_compare.append(line)
            else:
                sum += compare_threes(current_compare)
                current_compare = [line]

        sum += compare_threes(current_compare)
                
        return(sum)



def helper(part1, part2):
    current_items = []
    for item in part1:
        if item in part2 and item not in current_items:
            current_items.append(item)
    return current_items

def compare_threes(current_compare):
    current_items = helper(current_compare[0], current_compare[1])
    if len(current_items) > 1:
        final_letter = helper(str(current_items), current_compare[2]) 
    
    if final_letter[0].isupper():
        return ord(final_letter[0]) - 38
    else:
        return ord(final_letter[0]) - 96



print(part2())


