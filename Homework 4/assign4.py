"""
Name: Nam Huynh
ID: nsh1507
"""

"""Exercise 1a"""


def fSelect(lst, index):
    less = []
    same = []
    more = []
    if lst != []:
        first_element = lst[0]
        for element in lst:
            if element < first_element:
                less.append(element)
            elif element == first_element:
                same.append(element)
            elif element > first_element:
                more.append(element)
    if lst == []:
        return False
    elif index < len(less):
        return fSelect(less, index)
    elif (len(less) <= index) and (index < (len(less) + len(same))):
        return lst[0]
    elif (len(less) + len(same)) <= index:
        return fSelect(more, index - (len(less) + len(same)))


"""Exercise 1b"""


def iSelect(array, index):
    if index < 0 or index >= len(array):
        return False
    return iSelectHelper(array, index, 0, len(array) - 1)


def iSelectHelper(array, index, l, h):
    pivot_index = partition(array, l, h)
    if pivot_index == index:
        return array[pivot_index]
    elif pivot_index < index:
        l = pivot_index + 1
        return iSelectHelper(array, index, l, h)
    else:
        h = pivot_index - 1
        return iSelectHelper(array, index, l, h)


def partition(a, l, h):
    x = a[l]
    i = l + 1
    j = h
    while i <= j:
        if a[i] <= x:
            i += 1
        elif x < a[j]:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
    a[l], a[i - 1] = a[i - 1], a[l]
    return i - 1


"""Exercise 2a"""


def max2(num1, num2):
    abs_diff = abs(num1 - num2)
    max_val = (num1 + num2 + abs_diff) / 2

    return max_val
