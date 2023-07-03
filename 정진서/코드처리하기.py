def solution(code):
    answer = ''
    mode = 0
    ret = []
    code_list = [char for char in code]
    for i in range(len(code_list)):
        if code_list[i] == '1' and mode == 1:
            mode = 0
        elif code_list[i] == '1' and mode == 0:
            mode = 1
        if mode == 0 and i % 2 == 0 and code_list[i] != '1':
            ret += code_list[i]
        elif mode == 1 and i % 2 != 0 and code_list[i] != '1':
            ret += code_list[i]
    return ret

code = 'abc1abc1abc'

solution(code)