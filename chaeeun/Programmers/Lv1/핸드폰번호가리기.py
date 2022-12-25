def solution(phone_number):
    str = ""
    for i in range(len(phone_number)-4):
        str += '*'
    str += phone_number[-4:]
    return str
