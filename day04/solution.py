# from pprint import pprint as print
from elf import Elf

def main(test=True):
    file = "test.txt" if test else "input.txt"

    raw_data = [line.strip() for line in open(file).readlines()]
    # print(raw_data)

    elfs = []
    counter = 0
    pairs = []
    for elfpair in raw_data:
        elf_a = Elf(elfpair.split(",")[0])
        elf_b = Elf(elfpair.split(",")[1])
        
        counter += elf_a.is_fully_contained(elf_b)
        # print(tuple(elf_a.intersection(elf_b)))
        if tuple(elf_a.intersection(elf_b)) != ():
            pairs.append(tuple(elf_a.intersection(elf_b)))
    print(f"Part one: {counter}")
    print(f"Part two: {len(pairs)}")


if __name__ == '__main__':
    main(test=False)