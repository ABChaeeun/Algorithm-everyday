dict_num = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def solution(s):

    ### ver1 - key만으로 접근
    for key in dict_num:
        if key in s:
            s = s.replace(key, dict_num[key])

    ### ver2 - key, value로 접근
    # for key, value in dict_num.items():
    #     if key in s:
    #         s = s.replace(key, value)

    ### ver3 - 노가다
    # if 'zero' in s:
    #     s = s.replace('zero', '0')
    # if 'one' in s:
    #     s = s.replace('one', '1')
    # if 'two' in s:
    #     s = s.replace('two', '2')
    # if 'three' in s:
    #     s = s.replace('three', '3')
    # if 'four' in s:
    #     s = s.replace('four', '4')
    # if 'five' in s:
    #     s = s.replace('five', '5')
    # if 'six' in s:
    #     s = s.replace('six', '6')
    # if 'seven' in s:
    #     s = s.replace('seven', '7')
    # if 'eight' in s:
    #     s = s.replace('eight', '8')
    # if 'nine' in s:
    #     s = s.replace('nine', '9')

    answer = int(s)
    return answer


# print(solution("one4seveneight"))
# print(solution("23four5six7"))
# print(solution("2three45sixseven"))
# print(solution("123"))
