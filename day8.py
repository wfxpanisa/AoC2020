#!/usr/bin/bash

def simulate_boot_code(data, backtracking=False):
    lookup = set()
    acc = 0
    line = 0
    while True and line < len(data):
        if line in lookup:
            if backtracking:
                return False
            break
        lookup.add(line)
        ins, val = data[line]
        val = int(val)
        if ins == 'acc':
            acc += val
        elif ins == 'jmp':
            line += val-1
        line += 1
    return acc


def fst(data):
    return simulate_boot_code(data)

def snd(code):
    line = -1
    # using [:] avoids python's dumb reference sharing
    data = code[:]
    r = False
    while not r:
        line += 1
        r = simulate_boot_code(data, backtracking=True)
        data = code[:]
        ins, val = data[line]
        if ins == 'jmp':
            data[line] = ('nop', val)
        elif ins == 'nop':
            data[line] = ('jmp', val)
    return r

if __name__ == '__main__':
    lines = open('/tmp/test.txt', 'r').readlines()
    lines = open('/tmp/input.txt', 'r').readlines()
    data = [tuple(line.strip().split(' ')) for line in lines]
    print(fst(data))
    print(snd(data))
