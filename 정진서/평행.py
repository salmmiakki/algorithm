def solution(dots):
    if abs(dots[0][0] - dots[1][0]) == abs(dots[2][0] - dots[3][0]) and abs(dots[0][1] - dots[1][1]) == abs(dots[2][1] - dots[3][1]):
        print(1)
    elif abs(dots[0][0] - dots[2][0]) == abs(dots[1][0] - dots[3][0]) and abs(dots[0][1] - dots[2][1]) == abs(dots[1][1] - dots[3][1]):
        print(1)
    elif abs(dots[0][0] - dots[3][0]) == abs(dots[1][0] - dots[2][0]) and abs(dots[0][1] - dots[3][1]) == abs(dots[1][1] - dots[2][1]):
        print(1)
    else:
        print(0)

dots = [[1, 0], [9, 2], [3, 8], [11, 6]]
solution(dots)