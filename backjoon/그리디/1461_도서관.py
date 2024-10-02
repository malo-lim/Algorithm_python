import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
locations = list(map(int, input().split()))

pos = [] # 양수
neg = [] # 음수

for x in locations:
    if x > 0:
        pos.append(x)
    else:
        neg.append(-x)

pos = sorted(pos)[::-1] # 내림차순 정렬
neg = sorted(neg)[::-1] # 내림차순 정렬

dists = []

for p in pos[::M]:
    dists.append(p)

for n in neg[::M]:
    dists.append(n)

# 왔다 갔다 해야 하기 때문에 곱하기 2를 해주고, 큰 값은 마지막 방문이기 때문에 그 값을 빼준다.
result = 2 * sum(dists) - max(dists)

print(result)

"""
1. 양수와 음수로 나누어서 값을 append 한다. (음수도 양수로 집어 넣는다.)
2. 양수와 음수를 내림차순 정렬한다.
3. 양수와 음수를 M만큼 건너 뛰면서 dists에 값을 append 한다.
4. 그리고 2 * sum(dists)를 한 후 마지막에 한번만 방문할 제일 큰 값 을(max(dists)) 한번 빼준다.
    - * 2를 해주는 이유는 왔다 갔다 해야 하기 때문이다.
"""