def solution(a, b, c, d):
    answer = 0
    dice_count = [a,b,c,d]
    tmp = {a,b,c,d}
    dice = list(tmp)

    if len(dice) == 1:
        answer = dice[0] * 1111
    elif len(dice) == 2:
        if dice_count.count(dice[0]) == 2:
            answer = (dice[0] + dice[1]) * abs(dice[0] - dice[1])
        elif dice_count.count(dice[0]) == 3:
            answer = (10 * dice[0] + dice[1]) ** 2
        else:
            answer = (10 * dice[1] + dice[0]) ** 2
    elif len(dice) == 3:
        if dice_count.count(dice[0]) == 2:
            answer = dice[1] * dice[2]
        elif dice_count.count(dice[1]) == 2:
            answer = dice[0] * dice[2]
        else:
            answer = dice[0] * dice[1]
    elif len(dice) == 4:
        answer = min(dice)
    print(answer)
    return answer


a = 1
b = 1
c = 3
d = 4
solution(a, b, c, d)