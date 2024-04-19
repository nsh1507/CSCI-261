"""
Name: Nam Huynh
ID: nsh1507
"""


def head(lst):
    """Time complexity: O(1)"""
    return lst[0]


def tail(lst):
    """Time complexity: O(N)"""
    return lst[1:]


"""Exercise 1"""


def r(lst):
    if lst == []:
        return []
    else:
        return r(tail(lst)) + [head(lst)]


"""Exercise 2"""


def prod(m, n):
    if m == 0:
        return 0
    else:
        return prod(m - 1, n) + n


"""Exercise 3"""


def fastPow(b, k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return fastPow(b * b, k/2)
    elif k % 2 == 1:
        return fastPow(b * b, (k-1)/2) * b


"""Exercise 4"""


def prodAccum(m, n, a):
    if m == 0:
        return a
    else:
        return prodAccum(m-1, n, n+a)


"""Exercise 5"""


def minChange(a, lst):
    if a == 0:
        return 0
    elif lst == []:
        return None
    elif head(lst) > a:
        return minChange(a, tail(lst))
    else:
        return min(add(1, minChange(a - head(lst), lst)), minChange(a, tail(lst)))


def min(first_num, second_num):
    if first_num is None and second_num is None:
        return None
    elif first_num is None and second_num is not None:
        return second_num
    elif first_num is not None and second_num is None:
        return first_num
    if first_num >= second_num:
        return second_num
    elif second_num > first_num:
        return first_num


def add(first_num, second_num):
    if first_num is None or second_num is None:
        return None
    else:
        return first_num + second_num


"""Exercise 6"""


def greedyMinChange(a, lst):
    if a == 0:
        return 0
    elif lst == []:
        return None
    elif head(lst) > a:
        return greedyMinChange(a, tail(lst))
    else:
        q = a//head(lst)
        remainder = a % head(lst)
        return addGreedy(q, greedyMinChange(remainder, tail(lst)))


def addGreedy(first_num, second_num):
    if first_num is None or second_num is None:
        return None
    else:
        return first_num + second_num


"""
Exercise 7:
    a) 
        powIt(b,0;a)    =   a
        powIt(b,n;a)    =   powIt(b,n - 1; b x a)
    b)
        def powIt(b,n;a) :
            if  n=1 :
                return a
            else :
                return powIt(b,n-1; b x a)  
    c)
        def powIt(b,n;a) :
            a ← 1
            while n ≠ 1 : 
                n ← n − 1 
                a ← b x a
            return a
"""


def powIt(base, exponent):
    accum = 1
    while exponent > 0:
        exponent = exponent - 1
        accum = base * accum
    return accum
