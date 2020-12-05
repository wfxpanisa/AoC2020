#!/usr/bin/python3

def fst(trees):
    return search_slope(trees, 3, 1)

def snd(trees):
    from functools import reduce
    lst = []
    lst.append(search_slope(trees, 1, 1))
    lst.append(search_slope(trees, 3, 1))
    lst.append(search_slope(trees, 5, 1))
    lst.append(search_slope(trees, 7, 1))
    lst.append(search_slope(trees, 1, 2))
    return reduce(lambda x,y: x*y, lst)

def search_slope(trees, right, down):
    # acumulator
    tree_count = 0

    # starting position

    xpos = 0
    ypos = 0

    # auxiliary consts
    tlen = len(trees[0])
    row_count = len(trees)

    while ypos < row_count-1:
        # if current position is a tree, acumulate
        if trees[ypos][xpos] == '#':
            tree_count += 1

        # walk the slope movement
        xpos += right
        # "repeat" the three pattern by modding the value
        xpos %= tlen
        ypos += down

    return tree_count

if __name__ == '__main__':
    trees = open('/tmp/input.txt', 'r').read().split('\n')
    print(fst(trees))
    print(snd(trees))
