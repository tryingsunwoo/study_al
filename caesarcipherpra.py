def solution(s, n):
    ans = []
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for b in range(len(s)):
        if s[b].islower():
            c = a.index(s[b])
            if c + n < len(a):
                ans.append(a[c + n])
            else:
                ans.append(a[c + n - 26])
        elif s[b] == ' ':
            ans.append(' ')
        else:
            d = s[b].lower()
            c = a.index(d)
            if c + n < len(a):
                ans.append(a[c + n].upper())
            else:
                ans.append(a[c + n - 26].upper())
    answer = ''.join(ans)

    return answer

'''
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.
'''