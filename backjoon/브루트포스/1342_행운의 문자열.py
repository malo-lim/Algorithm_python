import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()

def fact(x):
    if x == 0:
        return 1
    return fact(x - 1) * x

S = input()
answer = 0

for permutation in permutations(S, len(S)):
    is_ok = True
    for i in range(len(S) - 1):
        if permutation[i] == permutation[i + 1]:
            is_ok = False
            break

    answer += is_ok

# a ~ z 까지 돌면서 문자 안에 들어있는 개수를 센 후 팩토리얼로 나누어준다.
for i in range(ord('a'), ord('z') + 1):
    answer //= fact(S.count(chr(i)))     

print(answer)