#!/usr/bin/python3
from itertools import combinations

#data = sorted([int(line) for line in open('/tmp/test.txt', 'r').readlines()])
#data = sorted([int(line) for line in open('/tmp/test2.txt', 'r').readlines()])
data = sorted([int(line) for line in open('/tmp/input.txt', 'r').readlines()])

datahead = 0
datatail = max(data) + 3
dataset = set(data)

def fst(lines, first, last):
    diffs = generate_diffs(first, lines, last)
    return diffs.count(1) * diffs.count(3)

def generate_diffs(first, lines, last):
    lines = [first] + lines + [last]
    return [lines[index+1]-lines[index] for index in range(len(lines)-1)]

def newsnd(head, body, tail):
    x = generate_diffs(head, body, tail)
    z = 0
    a = 1
    for i in x:
        if i == 1:
            z += 1
        else:
            if z > 1:
                if z == 4:
                    a *= 7
                if z == 3:
                    a *= 4
                if z == 2:
                    a *= 2
            z = 0
    return a

if __name__ == '__main__':
    print(fst(data, 0, max(data)+3))
    print(newsnd(datahead, data, datatail))
