import sys
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for permutation in permutations(range(1, N + 1), N):
    print(' '.join(map(str, permutation)))