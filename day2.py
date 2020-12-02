
def first_easy(passwords):
    # return accumulator
    valid_count = 0

    #iterating over each line of the input
    for pw in passwords:

        # parsing the line in a easy to use way
        rule, passw = pw.split(':')
        counts, ch = rule.split(' ')
        minch, maxch = [int(e) for e in counts.split('-')]
        passw = passw.strip()

        # checking ocurrences amount of char in password
        amount = passw.count(ch)
        if minch <= amount and amount <= maxch:
            # adding to the accumulator
            valid_count += 1
    return valid_count

def second_easy(passwords):
    # XOR Truth table ->  ^
    # 0 0 -> 0
    # 1 0 -> 1
    # 0 1 -> 1
    # 1 1 -> 0

    # return accumulator
    valid_count = 0

    #iterating over each line of the input
    for pw in passwords:

        # parsing the line in a easy to use way
        rule, passw = pw.split(':')
        counts, ch = rule.split(' ')
        fst_index, snd_index = [int(e) for e in counts.split('-')]
        passw = passw.strip()

        # XOR Operation on normalized index for the correct char
        if (passw[fst_index-1] == ch) ^ (passw[snd_index-1] == ch):
            valid_count += 1

    return valid_count


if __name__ == '__main__':
    # just loading our input into a list
    passwords = [e.strip() for e in open('/tmp/input.txt', 'r').readlines()]
    #print(first_easy(passwords))
    print(second_easy(passwords))
