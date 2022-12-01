# from pprint import pprint as print

stacks = {}
instructions = []

def input_parser(filename):
    raw = ["".join(list(line)[:-1]) for line in open(filename).readlines()]
    for line in raw:
        if '[' in line:                                                     # This is a line where the stack is being build
            indices = [i+1 for i, x in enumerate(line) if x == "["]         # get all indexes of letters, char before is always "["
            stack_numbers = list(map(lambda x: 1+int(x/4), indices))        # 1 col is max 4 chars wide, divide by 4 to get stack-number

            for countIndex, loc in enumerate(indices):
                s = stack_numbers[countIndex]
                letter = line[loc]

                if s not in stacks:
                    stacks.update({s: []})
                stacks[s].append(letter)

        elif 'move' in line:
            instructions.append([int(word) for word in line.split(" ") if word.isdigit()])

    for stack in stacks:
        stacks[stack].reverse()         #WE've added everything from top to bottom, 

def parse_instructions(CrateMover=9000):
    # print(stacks)
    for instruction in instructions:
        number = instruction[0]
        fr0m = instruction[1]
        t0 = instruction[2]

        MovedCrates = stacks[fr0m][-number:]
        if CrateMover == 9000:
            MovedCrates.reverse() 
        stacks[t0].extend(MovedCrates)
        stacks[fr0m] = stacks[fr0m][:-number]

    
def main(test=True):
    input_parser("input.txt" if not test else "test.txt")
    parse_instructions(CrateMover=9001)

    answer = ''
    for i in range(1, len(stacks)+1):
        answer += stacks[i][-1]

    print(answer)



if __name__ == '__main__':
    main(test=False)