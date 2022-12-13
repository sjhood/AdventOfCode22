
def read_in():
    actions = []
    current_state = []
    with open('input2.txt') as f:
        for line in f:
            if '[' in line:
                x=4
                res = [line.replace('\n', '')[y-x:y] for y in range(x, len(line.replace('\n', ''))+x,x)]
                for (index, item) in enumerate(res):
                    if '[' in item:
                        if len(current_state) < 1:
                            current_state = res
                            for index2, state in enumerate(current_state):
                                current_state[index2] = state.replace('[', '').replace(']', '').replace(' ', '')
                        else:
                            current_state[index] += item.replace('[', '').replace(']', '').replace(' ', '')
            elif 'move' in line:
                response = line.split()
                actions.append([response[1], response[3], response[5]])
    return current_state, actions


def do_actions(current_state, actions):
    for action in actions:
        for x in range(int(action[0])):
            # move from 1 to 2
            first = int(action[1]) - 1
            second = int(action[2]) - 1
            temp = current_state[first][0]
            current_state[first] = current_state[first][1::]
            current_state[second] = temp + current_state[second]
    return current_state

def do_actions_2(current_state, actions):
    for action in actions:
        first = int(action[1]) - 1
        second = int(action[2]) - 1
        temp = current_state[first][0:int(action[0])]
        current_state[first] = current_state[first][int(action[0])::]
        current_state[second] = temp + current_state[second]
    return current_state

def get_tops(current_state):
    tops = ''
    for item in current_state:
        tops += item[0]
    return tops


state, actions = read_in()
current_state = do_actions_2(state, actions)
print(get_tops(current_state))