import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

# 맨 앞에 0 을 넣어준다. 위치를 1부터 시작하기 위해
arr = [[0] + list(map(int, input().split())) for _ in range(N)]

# 배열 맨 앞에 M개의 길이를 가지는 배열 을 넣어준다.
# 이것도 마찬가지로 1부터 시작하기 위해
arr = [[0] * (M + 1)] + arr

# dp 를 0으로 전부 초기화 해준다.
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] += max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + arr[i][j]

print(dp[N][M])