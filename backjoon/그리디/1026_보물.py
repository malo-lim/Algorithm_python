import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0

for _ in range(N):
    answer += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))

print(answer)