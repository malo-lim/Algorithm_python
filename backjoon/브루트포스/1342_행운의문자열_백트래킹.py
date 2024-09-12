import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(level):
    global S, chars, count, choose, answer

    # base case
    if level == len(S):
        answer += 1
        return

    # recursive case
    for c in chars:
        if count[c] == 0:
            continue

        # 행운의 문자 판단, 이전 문자와 비교해서 아니어야함
        if (not choose) or (choose[-1] != c):
             count[c] -= 1
             choose.append(c)
             solution(level + 1)
             count[c] += 1
             choose.pop()

S = input()
chars = set()
count = dict()

for c in S:
    chars.add(c)

    if c not in count:
        count[c] = 0
    count[c] += 1 

choose = []
answer = 0

solution(0)

print(answer)