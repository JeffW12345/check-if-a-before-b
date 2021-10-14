def solution(S):
    string = S
    if 'a' not in string:
        return True
    string_as_list = list(string)
    a_yet = False
    b_yet = False
    for char in string_as_list:
        if char == 'a':
            a_yet = True
        if char == 'b':
            b_yet = True
        if char == 'b' and a_yet is False:
            return False
        if char == 'a' and b_yet is True:
            return False
    return True

S = "aabbb"
print(solution(S)) # Expected output True
S = "ba"
print(solution(S)) # Expected output False
S = "aaa"
print(solution(S)) # Expected output True
S = "b"
print(solution(S)) # Expected output True
S = "abba"
print(solution(S)) # Expected output False
