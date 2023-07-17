def solution(array):
    answer = 0
    result = {item: array.count(item) for item in array}
    max(result,key=result.get) # result.get 이용
    answer = [k for k,v in result.items() if max(result.values()) == v]
    if len(answer) > 1:
        print(-1)
    else:
        end = int(answer[0])
        print(end)
        print(type(end))

array = [1, 1, 2, 2]

solution(array)