from aocd import get_data, submit
raw_data = get_data(day=1, year=2022)
# print(raw_data)

from elf import Elf

Elfs = [Elf(caloriedata) for caloriedata in raw_data.split('\n\n')]
Calories = [e.total_calories for e in Elfs]
Calories.sort(reverse=True)

# part_one = max([e.total_calories for e in Elfs])
# print(part_one)
# response = submit(part_one)


# part_two = sum(Calories[:3])
# print(part_two)
# submit(part_two)