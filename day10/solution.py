
from functools import reduce 


instructions = [line.strip().split(" ") for line in open("input.txt").readlines()]
x = [1]
cycles = 0
CRT = []

def parse_instruction(instruction):
    if len(instruction) == 1:
        CRT.append("\U00002B1C" if abs(x[-1]-(len(CRT) % 40 )) < 2 else "\U00002B1B")
        x.append(x[-1])
        return 1
    
    if instruction[0].startswith("add"):
        CRT.append("\U00002B1C" if abs(x[-1]-(len(CRT) % 40 )) < 2 else "\U00002B1B")
        x.append(x[-1])
        CRT.append("\U00002B1C" if abs(x[-1]-(len(CRT) % 40 )) < 2 else "\U00002B1B")
        x.append(x[-1] + int(instruction[1]))
        return 2

for instruction in instructions:
    cycles += parse_instruction(instruction)

p1 = sum([ x[i-1]*i for i in [20, 60, 100, 140, 180, 220]])
print(f"Part one: {p1}\nPart two:")

for n in range(0, len(CRT)//40):
    print("".join(CRT[(n*40):(n+1)*40]))