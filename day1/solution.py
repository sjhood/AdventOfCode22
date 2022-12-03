
# no focus on efficiency, just playin around

def part_1():
    current_max_value = 0
    current_elf_value = 0

    with open('input.txt', 'r') as file:
        for line in file:
            if len(line) > 1:
                current_elf_value += int(line)
            else:
                if current_max_value < current_elf_value:
                    current_max_value = int(current_elf_value)
                current_elf_value = 0



def part_2():
    current_max_values = [0, 0, 0]
    current_elf_value = 0

    with open('input.txt', 'r') as file:
        for line in file:
            if len(line) > 1:
                current_elf_value += int(line)
            else:
                if current_max_values[2] <= current_elf_value:
                    current_max_values.append(int(current_elf_value))
                    current_max_values.sort(reverse=True)
                    del current_max_values[-1]

                current_elf_value = 0
            
        if current_max_values[2] <= current_elf_value:
            current_max_values.append(int(current_elf_value))
            current_max_values.sort(reverse=True)
            del current_max_values[-1]

    return sum(current_max_values)

