

def part_1():
    count = 0
    with open("/Users/hades/Programming/AdventOfCode22/day4/input2.txt") as file:
        for line in file:
            sections = line.split(',')
            for x in range(len(sections)):
                sections[x] = sections[x].replace('\n', '').split('-')
            
            if contains(sections[0], sections[1]) or contains(sections[1], sections[0]):
                count+=1

    return count

def contains(section1, section2):
    return (int(section1[0]) >= int(section2[0]) and int(section1[1]) <= int(section2[1]))

def overlaps(section1, section2):
    return int(section1[0]) >= int(section2[0]) and int(section1[0]) <= int(section2[1])

def part_2():
    count = 0
    with open("/Users/hades/Programming/AdventOfCode22/day4/input2.txt") as file:
        for line in file:
            sections = line.split(',')
            for x in range(len(sections)):
                sections[x] = sections[x].replace('\n', '').split('-')

            if overlaps(sections[0], sections[1]) or overlaps(sections[1], sections[0]):
                count += 1

    return count


print(part_2())