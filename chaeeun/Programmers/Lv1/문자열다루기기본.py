def solution(s):
    digit = s.isdigit()
    length = len(s)
    if (length == 4 or length == 6) and digit:
        return True
    else:
        return False