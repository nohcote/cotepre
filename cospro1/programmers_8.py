# 다음과 같이 import를 사용할 수 있습니다.
# import math
import copy

def fill1(arr, x, y, xmax, ymax):
    if x-1 >= 0:
        arr[x-1][y] = 1
    if x+1 < xmax:
        arr[x+1][y] = 1
    if y-1 >= 0:
        arr[x][y-1] = 1
    if y+1 < ymax:
        arr[x][y+1] = 1

def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0
    
    while True:
        if all([0 not in l for l in [l for l in garden]]):
            break
        answer += 1
        temparr = copy.deepcopy(garden)
        for i, line in enumerate(garden):
            for j, e in enumerate(line):
                if e == 1:
                    fill1(temparr, i, j, len(temparr), len(line))
        garden = temparr
    
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")