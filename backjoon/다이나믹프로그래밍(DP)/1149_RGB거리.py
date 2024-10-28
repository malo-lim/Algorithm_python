import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

cost = [[0, 0, 0]]

# cost 에 배열을 넣어준다.
cost += [list(map(int, input().split())) for _ in range(N)]

# dp 를 0으로 전부 초기화 해준다.
dp = [[0, 0, 0] for _ in range(N + 1)]

for i in range(1, N + 1):
    # 빨간색
    dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])

    # 초록색
    dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])

    # 파란색
    dp[i][2] = cost[i][2] + min(dp[i - 1][0],  dp[i - 1][1])


print(min(dp[N]))    

"""    
빨간집, 초록집, 파란집인 경우를 계산하는데 그 이전의 값들 중에서 같은 색을 제외하고 최솟값을 더해주는걸 반복한다.  
빨강, 초록, 파랑 집을 선택한 모든 경우에 대  해 최솟값만이 더해져서 나오게 되며 이중에 최소 값을 선택하면 된다.
"""