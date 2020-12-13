
def is_sum_possible(preamble, target):
    # remove duplicated entries
    s = set(preamble)
    # check for a pair of sums
    for a in s:
        for b in s:
            if a + b == target and a is not b:
                # return if conditions holds
                return True
    return False

def fst(lines):
    preamble_size = 25
    start = 0
    # while the range is matching, increase the head pointer
    while is_sum_possible(lines[start:start + preamble_size], lines[start + preamble_size]):
        start += 1

    return lines[start+preamble_size]

def snd(lines, target):
    start, end = 0, 1
    while True:
        aux = sum(lines[start:end])
        # if it is too low, increase the size by expanding the tail
        if aux < target:
            end += 1
        # if it is too high, decrease the size by contracting the head
        elif aux > target:
            start += 1
        else:
            return min(lines[start:end]) + max(lines[start:end])


if __name__ == '__main__':
    #lines = [int(line) for line in open('/tmp/test.txt', 'r').readlines()]
    lines = [int(line) for line in open('/tmp/input.txt', 'r').readlines()]
    print(snd(lines, fst(lines)))
