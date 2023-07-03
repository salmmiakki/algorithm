M = int(input())
N = int(input())

check = 0
sum = 0
if M == 1:
    M = M + 1

for i in range(M, N + 1): ## 소수인지 판별할 수 i
    for j in range(2, i): ## i에 대해서 소수 판별
        if i % j == 0: ## i가 소수가 아니면
            check -= i
            break
    check += i ## 소수면 check 는 소수인 i 의 합
    if check <= i: ## 소수인 i 의 최소값 구하기
        sum = check

if check == 0:
    print(-1)
else:
    print(check)
    print(sum)
