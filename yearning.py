def solution(name, yearning, photo):
    answer = []
    name_dict = {name:value for value, name in zip(yearning, name)}
    #print(name_dict)
    for i in photo: ## photo 의 1차원 배열
        result = 0
        for j in i: ## photo 의 1차원 배열의 원소
            if j in name: ## photo의 1차원 배열의 원소가 name에 있으면
                result += yearning[name.index(j)] ## name의 index와 yearning의 index
                print(name.index(j))
        answer.append(result)
    return answer


name = ["may", "kein", "kain", "radi"]	
yearning = [5, 10, 1, 3]	
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

solution(name, yearning, photo)