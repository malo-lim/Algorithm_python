import sys
input = lambda: sys.stdin.readline().rstrip()

vows = ["a", "e", "i", "o", "u"]  # 모음
choose = []

def is_possible():
    global L, C, choose, arr
    vow = 0
    for c in choose:
        vow += c in vows
    con = L - vow
    
    return vow >= 1 and con >= 2


def combination(index, level):
    if level == L:
        if is_possible():
            print("".join(choose))
        return

    for i in range(index, C):
        choose.append(arr[i])
        combination(i + 1, level + 1)
        choose.pop()


L, C = list(map(int, input().split()))
arr = input().split()
arr.sort()

combination(0, 0)
