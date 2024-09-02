import sys

input = lambda: sys.stdin.readline().rstrip()
lotto_count = 6


def combination(index, level):
    global choose, arr, k
    if level == lotto_count:
        for u in choose:
            print(u, end=" ")
        print()
        return

    for i in range(index, k):
        choose.append(arr[i])
        combination(i + 1, level + 1)
        choose.pop()


while True:
    choose = []
    lotto = list(map(int, input().split()))

    k = lotto[0]
    arr = lotto[1:]

    if k == 0:
        break

    combination(0, 0)
    print()
