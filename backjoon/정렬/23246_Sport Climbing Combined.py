import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
humans = [list(map(int, input().split())) for _ in range(N)]
humans = sorted(humans, key=lambda x: (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))

for b, p, q, r in humans[:3]:
    print(b, end=' ')