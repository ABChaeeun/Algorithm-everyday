def solution(new_id):
    ##### 1. 모두 소문자로
    new_id = new_id.lower()

    ##### 2. 이상한 문제 제거
    for i in new_id:
        if i in '~!@#$%^&*()=+[{]}:?,<>/':
            new_id = new_id.replace(i, '')

    ##### 3. 마침표 여러개 하나로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    ##### 4. 처음이나 끝에 있는 마침표 제거
    # new_id = new_id.strip('.')
    if len(new_id) != 0:
        if new_id[0] == '.':
            new_new = ''
            new_new += new_id[1:]
            new_id = new_new
    if len(new_id) != 0:
        if new_id[-1] == '.':
            new_new = ''
            new_new += new_id[:-1]
            new_id = new_new

    ##### 5. 빈 문자열이면 'a' 추가
    if len(new_id) == 0:
        new_id += 'a'

    ##### 6. 15 초과면 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')

    ##### 7. 2자 이하면 3자까지 채우기
    if len(new_id) <= 2:
        while (len(new_id) < 3):
            new_id += new_id[-1]
            if len(new_id) == 3:
                break

    answer = new_id
    return answer

# print(solution('~!@#$%^&*()=+[{]}:?,<>/'))
# print(solution('...!@BaT#*..y.abcdefghijklm'))
# print(solution('z-+.^.'))
# print(solution('=.='))
# print(solution('123_.def'))
# print(solution('abcdefghijklmn.p'))
