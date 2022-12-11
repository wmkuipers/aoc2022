from math import prod

class Monkey:
    def __init__(self, raw):
        self._throw_to = {}
        self._total_item_inspection = 0
        for line in raw:
            if line.startswith("  Starting items:"):
                self.items = [int(item) for item in line[17:].split(",")]

            if line.startswith("  Operation: "):
                op = line[13:].split(" ")
                self._value = int(op[-1]) if op[-1].isnumeric() else None
                self._monkey_operation = op[3]

            if 'throw to monkey' in line:
                stripped = line.strip().split(" ")
                self._throw_to.update({
                    stripped[1][:-1] == 'true' : int(stripped[-1])
                })

            if 'divisible by' in line:
                self._divisible_by = int(line.strip().split(" ")[-1])
            
    def new_worry_level(self, worry_level):
        match self._monkey_operation:
            case "*":
                monkey_operation = prod
            case "+":
                monkey_operation = sum
        return monkey_operation([worry_level, self._value]) if self._value else monkey_operation([worry_level, worry_level])

    def receive_item(self, item):
        self.items.append(item)

    def play_with_items(self, all_monkeys, modulus=None):
        for item in self.items:
            self._total_item_inspection += 1
            
            if modulus is None:
                new_worry_level = self.new_worry_level(item) // 3
            else:
                new_worry_level = self.new_worry_level(item) % modulus
            all_monkeys[self._throw_to[(new_worry_level % self._divisible_by) == 0]].receive_item(new_worry_level)

        self.items = []
