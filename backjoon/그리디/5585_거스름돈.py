import sys
input = lambda: sys.stdin.readline().rstrip()

money = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
answer = 0

for coin in coins:
    answer += money // coin
    money %= coin

print(answer)