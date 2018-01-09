#    How to run doctest:
#    python -m doctest -v stats.py


def add(num1, num2):
    return num1 + num2


def volume(length, width, height):
    return length * width * height


def mean(numbers):
    return sum(numbers) / len(numbers)

# 39127
# sort -> 12379
# middle -> 3

# 391274
# sort -> 123479
# avg of middle -> 3+4/2 -> 3.5


def median(numbers):
    """Computes the median of a list of numbers.

    argument: list of numbers
    return: the median

    >>> median([2,1,6])
    2
    >>> median([3,5,4,9])
    4.5

    """
    numbers = sorted(numbers)
    middle = len(numbers) // 2 # use '//' for integer division
    if len(numbers) % 2 == 0:
        # even list
        return sum(numbers[middle - 1:middle + 1]) / 2
    else:
        # odd list
        return numbers[middle]

from collections import defaultdict
def mode(numbers):
    """Find the most common value in the list

    argument: list of numbers
    return: the mode

    >>> mode([1,2,2,2,3,3,4])
    2
    """
    d = defaultdict(int)
    for num in numbers:
        d[num] += 1
    return sorted(d, key=lambda k: d[k])[-1]
