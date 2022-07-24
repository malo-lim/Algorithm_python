# 30) 중복 문자 없는 가장 긴 부분 문자열

def length_of_longest_substring(s: str) -> int:
    used = {}
    max_length = start = 0

    for index, char in enumerate(s):
        # 이미 등장 했던 문자라면
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            # 최대 부분 문자열 길이 갱신
            max_length = max(max_length, index - start + 1)

        # 현재 문자의 위치 삽입
        used[char] = index

    return max_length

print(length_of_longest_substring('abcabcbb'))