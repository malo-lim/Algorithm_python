# 31) 상위 K 빈도 요소

import collections
import heapq
from typing import List

# Counter를 이용한 방식
def top_k_frequent_counter(data: List[int], k: int) -> List[int]:
    dic = collections.Counter(data)
    dic_heap = []

    # 힙에 음수로 저장
    for f in dic:
        heapq.heappush(dic_heap, (-dic[f], f))

    top_k = list()
    # k번 만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        top_k.append(heapq.heappop(dic_heap)[1])

    return top_k

# 파이썬 다운 방식
def top_k_frequent_python(data: List[int], k: int) -> List[int]:
    return list(zip(*collections.Counter(data).most_common(k)))[0]

nums = [1,1,1,2,2,3,4]
k = 2

print(top_k_frequent_counter(nums, k))
print(top_k_frequent_python(nums, k))