
import numpy as np
direction_delta = {
    "R": np.array([1,0]),
    "U": np.array([0,1]),
    "L": np.array([-1,0]),
    "D": np.array([0,-1])
}



class Rope:
    
    def __init__(self):
        self._head_position = []
        self._tail_position = []

        self._head_position.append(np.array([0,0]))
        self._tail_position.append(np.array([0,0]))

    def _move_direction(self, dir):
        self._head_position.append(
            np.add(self._head_position[-1], direction_delta[dir])
        )

        self.calculate_tail()
    
    
    def _add_delta(self, delta):
        if max(delta) > 1:
            print(delta)
            np.add(self._head_position[-1], delta)
        self.calculate_tail()

    def calculate_tail(self):
        delta = abs(self._head_position[-1] - self._tail_position[-1])
        if max(delta > 1):
            self._tail_position.append(
                self._head_position[-1]
            )
        else:
            self._tail_position.append(
                self._tail_position[-1]
            )

    @property
    def unique_tail_positions(self):
        return len({tuple(p) for p in self._tail_position})

    @property
    def unique_head_positions(self):
        return len({tuple(p) for p in self._head_position})

instructions = [{"dir": line.strip().split(" ")[0], "amount": int(line.strip().split(" ")[1])}  for line in open("test2.txt").readlines()]

rope = Rope()
for instruction in instructions:
    for i in range(0,instruction['amount']):
        rope._move_direction(instruction['dir'])

from pprint import pprint as print
print(f"Part one: {rope.unique_tail_positions}")


ropes = [Rope() for i in range(10)]
for instruction in instructions:
    for i in range(0,instruction['amount']):
        ropes[0]._move_direction(instruction['dir'])
        for index in range(1, 10):
            delta = abs(ropes[index]._head_position[-1] - ropes[index-1]._head_position[-1])
            ropes[index]._add_delta(delta)
            
print(f"Part two: {ropes[-1].unique_head_positions}")
print({tuple(p) for p in ropes[-1]._head_position})