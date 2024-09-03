import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]

dots = sorted(dots)

for x, y in dots:
    print(x, y)