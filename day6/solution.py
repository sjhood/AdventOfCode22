

def find_start(length):
    with open('input2.txt') as f:
        for line in f:
            for x in range(length, len(line)):
                if len(set(line[x-length:x])) == length:
                    return x


print(find_start(4))
print(find_start(14))