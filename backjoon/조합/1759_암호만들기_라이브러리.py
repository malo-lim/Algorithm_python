import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

vows = ["a", "e", "i", "o", "u"]  # 모음

def is_possible(word):
    global L, C, arr
    vow = 0
    for c in word:
        vow += c in vows
    con = L - vow
    
    return vow >= 1 and con >= 2

L, C = list(map(int, input().split()))
arr = input().split()
arr.sort()

for word in combinations(arr, L):
    if is_possible(word):
        print(''.join(word))
    