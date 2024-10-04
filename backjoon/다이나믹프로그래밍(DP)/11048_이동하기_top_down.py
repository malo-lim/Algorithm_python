import sys
sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()

def _dp(i, j):
    global arr, dp

    # base case
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = max(_dp(i - 1, j), _dp(i, j - 1), _dp(i - 1, j - 1)) + arr[i][j]
    return dp[i][j]

N, M = map(int, input().split())

# 맨 앞에 0 을 넣어준다. 위치를 1부터 시작하기 위해
arr = [[0] + list(map(int, input().split())) for _ in range(N)]

# 배열 맨 앞에 M개의 길이를 가지는 배열 을 넣어준다.
# 이것도 마찬가지로 1부터 시작하기 위해
arr = [[0] * (M + 1)] + arr

# dp 를 -1으로 전부 초기화 해준다.
dp = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]

# 배열 0 행과 0번째 인덱스 값을 0으로 초기화 한다. 값을 접근하지 않기 위해
for j in range(0, M + 1):
    dp[0][j] = 0

for i in range(0, N + 1):
    dp[i][0] = 0

print(_dp(i, j))