#!/usr/bin/python3

def snd(answers):
    groups = []
    # dictionary holding the amount of answers for each letter
    # and counting how many pp in a group
    # if both match, then we consider that answer
    aux = {}
    aux['pp'] = 0
    for line in lines:
        if line == '':
            groups.append(aux)
            aux = {}
            aux['pp'] = 0
        else:
            aux['pp'] += 1
            for e in line:
                if e not in aux:
                    aux[e] = 0
                aux[e] += 1

    # we start the counter at negative amount of groups, to prevent PP from counting as an answer
    count = -(len(groups))
    for group in groups:
        for answer in group.values():
            if answer == group['pp']:
                count += 1

    return count

def fst(answers):
    groups = []
    # a set of answers got from any participant of the group
    aux = set()
    for line in lines:
        if line == '':
            groups.append(aux)
            aux = set()
        else:
            [aux.add(e) for e in line]
    if aux != set():
        groups.append(aux)
    # we return sum of amount of unique answers
    return sum([len(e) for e in groups])

if __name__ == '__main__':
    lines = open('/tmp/input.txt', 'r').read().split('\n')
    print(fst(lines))
    print(snd(lines))
