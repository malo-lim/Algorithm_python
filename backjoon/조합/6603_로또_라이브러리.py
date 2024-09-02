import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

while True:
    lotto = list(map(int, input().split()))

    k = lotto[0]
    arr = lotto[1:]

    if k == 0:
        break

    for combination in combinations(arr, 6):
        for u in combination:
            print(u, end=" ")
        print()
    print()
