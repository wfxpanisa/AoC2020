# O(n*2) -> O(n)
def first_fast(numbers):
    lookup = {}
    target = 2020
    for a in numbers:
        lookup[target-a] = a
    for a in numbers:
        # if the difference to get to 2020 is in the lookup table
        # this means that we have a suitable pair to solve our problem
        if a in lookup:
            return lookup[a] * a

# O(n²)
def first_easy(numbers):
    # target is our search sum
    target = 2020
    # iterating twice to check all combinations
    for a in numbers:
        for b in numbers:
            if a + b == target:
                return a * b # return the product

# O(n³)
def second_easy(numbers):
    # target is our search sum
    target = 2020
    # iterating three times to check all combinations
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a + b + c == target:
                    return a * b * c # return the product

if __name__ == '__main__':
    # Read the input file and converts it to list of numbers (int)
    numbers = [int(x) for x in open('/tmp/input.txt', 'r').readlines()]
    print(first_easy(numbers))
    print(second_easy(numbers))
    print(first_fast(numbers))
