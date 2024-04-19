"""
ID:nsh1507
Name: Nam Huynh
"""

"""Exercise 1a"""


def search(array, value):
    l = 0
    h = len(array) - 1
    while l <= h:
        m = (h+l)//2
        if value == array[m]:
            return True
        elif value < array[m]:
            h = m - 1
        elif value > array[m]:
            l = m + 1
    return False


"""Exercise 4b"""


def sortedHasSum(array, x):
    l = 0
    h = len(array) - 1

    while l < h:
        curr_sum = array[l] + array[h]

        if curr_sum == x:
            return True
        elif curr_sum < x:
            l += 1
        else:
            h -= 1
    return False


"""Exercise 4c"""


def hasSum(array, x):
    array = merge_sort(array)
    return sortedHasSum(array, x)


def merge_sort(L):
    if L == []:
        return []
    elif len(L) == 1:
        return L
    else:
        (half1, half2) = split(L)
        return merge(merge_sort(half1), merge_sort(half2))


def split(L):
    evens = []
    odds = []
    is_even_index = True
    for e in L:
        if is_even_index:
            evens.append(e)
        else:
            odds.append(e)
        is_even_index = not is_even_index
    return evens, odds


def merge(sorted1, sorted2):
    result = []
    index1 = 0
    index2 = 0
    while index1 < len(sorted1) and index2 < len(sorted2):
        if sorted1[index1] <= sorted2[index2]:
            result.append(sorted1[index1])
            index1 = index1 + 1
        else:
            result.append(sorted2[index2])
            index2 = index2 + 1
    if index1 < len(sorted1):
        result.extend(sorted1[index1:])
    elif index2 < len(sorted2):
        result.extend(sorted2[index2:])
    return result


"""Exercise 4d"""


def quickSort(a):
    qSortHelp(a, 0, len(a)-1)
    return a


def qSortHelp(a, l, h):
    if l < h:
        m = partition(a, l, h)
        qSortHelp(a, l, m-1)
        qSortHelp(a, m+1, h)



def partition(a, l, h):
    x = a[l]
    i = l+1
    j = h
    while i <= j:
        if a[i] <= x:
            i += 1
        elif x < a[j]:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
    a[l], a[i-1] = a[i-1], a[l]
    return i - 1
