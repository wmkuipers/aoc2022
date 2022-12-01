#!/usr/bin/env python

import os
# from pprint import pprint as print

def get_score(char):
    if ord(char) in range(ord('a'), ord('z')+1):
        return ord(char) - ord('a') + 1
    else: 
        return ord(char) - ord('A') + 27

def main(test=False):
    raw_data = open("test.txt","r").readlines()
    # print(raw_data)

    s=[]
    for line in raw_data:
        l = line.strip()    # Actual line
        hL = len(l)//2      # length of halve the line
        lines = [set(l[:hL]), set(l[hL:])]
        overlap = list(set.intersection(lines[0], lines[1]))
        s.append(get_score(overlap[0]))

    # submit(sum(s))
    print(f"Part one: {sum(s)}")

    part_two = [ get_score(list(set.intersection(
            set(list(raw_data[i*3 + 0].strip())),
            set(list(raw_data[i*3 + 1].strip())),
            set(list(raw_data[i*3 + 2].strip()))
        ))[0]) for i in range(0, int(len(raw_data)/3)) ]

    print(f"Part two: {sum(part_two)}")




if __name__ == '__main__':
    main(test=True)