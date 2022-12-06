# from pprint import pprint as print

stacks = {}
instructions = []

def input_parser(filename):
    raw = [ line.strip() for line in open(filename).readlines()]
    return raw


def find_first_uniue_set(number, string):
    s = list(string)
    i = number
    while i < len(s):
        candidate = set(string[i-number:i])
        if len(candidate) == number:
            return i
        i+= 1

    
def main(test=True):
    data = input_parser("input.txt" if not test else "test.txt")[0]
    part_one = find_first_uniue_set(4, data)
    part_two = find_first_uniue_set(14, data)
    print(f"Part one: {part_one}")
    print(f"Part two: {part_two}")
    


if __name__ == '__main__':
    main(test=True)