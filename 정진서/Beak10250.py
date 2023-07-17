## ACM 호텔
N = int(input())

for _ in range(N):
    H, W, N = map(int, input().split())
    Y = 0  # 객실의 층

    if N % H == 0: # 꼭대기 층은 H
        Y = H
    else:
        Y = N % H # H의 배수로 층수가 정해짐

    cnt = (N - 1) // H + 1  # 객실의 호
                            # N / H + 1 하게되면 딱 나누어 떨어질 때 (꼭대기 층일 때) 호수에 + 1 이 되어버림
                            # 조건 하나 더 넣기 또는 N에서 1을 빼서 계산하는 방법으로 해결 가능

    print(Y * 100 + cnt)
