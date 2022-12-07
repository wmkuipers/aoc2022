# from pprint import pprint as print

stacks = {}
instructions = []

def input_parser(filename):
    raw = [ line.strip() for line in open(filename).readlines()]
    return raw


def find_first_uniue_set(number, string):
    i = number
    while i < len(string):
        candidate = set(string[i-number:i])
        if len(candidate) == number:
            return i
        i+= 1

    
def main(test=True):
    data = input_parser("aoc_2022_day06_extra_input.txt")[0]
    part_one = find_first_uniue_set(94, data)
    print(f"Part one: {part_one}")
    


if __name__ == '__main__':
    main(test=True)