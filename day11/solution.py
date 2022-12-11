from math import lcm

from monkeybusiness import Monkey

raw_monkeys = [line.split("\n") for line in open("input.txt").read().split("\n\n")]
all_monkeys = {no: Monkey(m) for no, m in enumerate(raw_monkeys)}

modulus = lcm(*[monkey._divisible_by for i, monkey in all_monkeys.items()])
print(modulus)

for round in range(10000):
    for i, monkey in all_monkeys.items():
        # print(f"Parsing monkey {i} for round {round}")
        monkey.play_with_items(all_monkeys, modulus=modulus)

    # for i, monkey in all_monkeys.items():
    #     print(f"Monkey {i}: {monkey.items}")

for i, monkey in all_monkeys.items():
    print(f"Monkey {i} inspected items {monkey._total_item_inspection}")

top_list = [monkey._total_item_inspection for i, monkey in all_monkeys.items()]
top_list.sort(reverse=True)
print(f"Part two: {top_list[0]*top_list[1]}")