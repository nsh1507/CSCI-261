from dataclasses import dataclass

"""
Name: Nam Huynh
ID: nsh1507
"""

"""Exercise 4a"""


def fibDyn(n):
    p = [0] * (n + 1)
    p[1] = 1
    for k in range(2, n + 1):
        p[k] = p[k - 1] + p[k - 2]
    return p[n]


"""Exercise 4b part d"""


@dataclass
class Item:
    value: int
    weight: int


def knapsack(capacity, lst):
    dp = [[0] * (capacity + 1) for _ in range(len(lst) + 1)],

    for i in range(1, len(lst) + 1):
        for w in range(1, capacity + 1):
            if lst[i - 1].weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                keep = lst[i - 1].value + dp[i - 1][w - lst[i - 1].weight]
                leave = dp[i - 1][w]
                dp[i][w] = max(keep, leave)

    return dp[len(lst)][capacity]


"""Exercise 4b part e"""


def knapsackContents(capacity, lst):
    dp = [[0] * (capacity + 1) for _ in range(len(lst) + 1)]

    for i in range(1, len(lst) + 1):
        for w in range(1, capacity + 1):
            if lst[i - 1].weight > w:
                dp[i][w] = dp[i - 1][w]

            else:
                keep = lst[i - 1].value + dp[i - 1][w - lst[i - 1].weight]
                leave = dp[i - 1][w]

                dp[i][w] = max(keep, leave)

    selected_items = []
    l, w = len(lst), capacity
    while l > 0 and w > 0:
        if dp[l][w] != dp[l - 1][w]:
            selected_items.append(lst[l - 1])
            w -= lst[l - 1].weight
        l -= 1

    return selected_items


weight = [Item(60, 10), Item(100, 20), Item(120, 30)]
print(knapsackContents(60, weight))
