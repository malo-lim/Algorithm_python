import sys
input = lambda: sys.stdin.readline().rstrip()

def recursion(k):
    # base case
    if k == 0:
        print("-", end="")
        return

    # recursive case
    recursion(k - 1)
    print(" " * (3 ** (k - 1)), end="")
    recursion(k - 1)


while True:
    try:
        N = int(input())
        recursion(N)
        print()
    except:
        break
