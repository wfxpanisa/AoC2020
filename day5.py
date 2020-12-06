#!/usr/bin/python3
def decode_string(code, upper_limit):
    lower_limit = 0
    for e in code:
        if e in ['F', 'L']:
            upper_limit = (lower_limit + upper_limit) // 2
        elif e in ['B', 'R']:
            # I think the +1 is needed just because we start at 0, but i'm not sure
            lower_limit = ((lower_limit + upper_limit) // 2) + 1
        else:
            raise Exception("bad code: ", e)
    return lower_limit if code[-1] in ['F', 'L'] else upper_limit

def get_seat_id(boarding):
    return decode_string(boarding[:7], 127) * 8 + decode_string(boarding[7:], 7)

def fst(boarding_list):
    return max([get_seat_id(item.strip()) for item in boarding_list])

def snd(boarding_list):
    seats = set([get_seat_id(item.strip()) for item in boarding_list])
    lst = []
    # generate a set with all seats filled and takes the diference from both sets
    for i in range(min(seats), max(seats)):
        lst.append(i)
    return max(set(lst).difference(seats))

if __name__ == '__main__':
    # test cases
    #print(get_seat_id('FBFBBFFRLR'))
    #print(get_seat_id('BFFFBBFRRR'))
    #print(get_seat_id('FFFBBBFRRR'))
    #print(get_seat_id('BBFFBBFRLL'))
    boarding_list = open('/tmp/input.txt', 'r').readlines()
    #print(fst(boarding_list))
    print(snd(boarding_list))
