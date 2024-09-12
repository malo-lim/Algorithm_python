import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for i in range(1, N + 1):
    for combination in combinations(arr, i):
        if sum(combination) == S:
            answer += 1

print(answer)