import sys
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
infos = [input().split() for _ in range(N)]
answer = 0

for cur in permutations(range(1,10), 3):
    is_ok = True

    for num, strike, ball in infos:
        cur_strike = cur_ball = 0

        for i in range(3):
            if str(cur[i]) == num[i]:
                cur_strike += 1
            elif str(cur[i]) in num:
                cur_ball += 1

        if cur_strike != int(strike) or cur_ball != int(ball):
            is_ok = False
            break

    if is_ok:
        answer += 1

print(answer)