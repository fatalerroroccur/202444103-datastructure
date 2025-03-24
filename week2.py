import random
try = 7
target = random.randint(1,100)
for chance in range(7):
    try = try-1
    answer=int(input("숫자를 입력"))
    if answer==target:
        print("정답")
        break
    elif answer > target:
        print("정답보다 큰수를 입력하였읍니다")
    else:
        print("정답보다 작은수를 입력하였읍니다")
    if try = 0:
        print("실패입니다")

