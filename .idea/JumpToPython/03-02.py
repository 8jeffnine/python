treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


# while문 직접 만들기
#  int(input())는 사용자의 숫자 입력을 받아들이는 것
prompt=['Add','Del','List','Quit']
number = 0
while number != 4:
    print(prompt[number])
    number = int(input())


# while문 강제로 빠져나가기 (break)
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# 커피 자동판매기
"""
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
"""

# while문의 맨 처음으로 돌아가기
# 1부터 10까지의 숫자 중에서 홀수만 출력하는 것을 while문을 이용해서 작성
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: continue
    print(a)


# exercise 1
# 1부터 100까지 더하기
a = 1
b = 0
while a <= 100:
    b = b+a
    if a == 100:
        print(b)
    a = a+1

# exercise 2
# 3의 배수의 합
a = 1
b = 0
while a <= 1000:
    if a % 3 == 0:
        b = b + a
    a = a+1
print(b)

# exercise 3
# 50점 이상의 총합
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
a = 0
b = 0
while a < len(A):
    if A[a] >= 50:
        b = b + A[a]
    a = a + 1
print(b)

# exercise 4
# while문을 이용하여 아래와 같이 별(*)을 표시하는 프로그램을 작성해 보자.
a=1
while a < 5:
    b=""
    while len(b) < a:
        b = b+"*"
    print(b)
    a = a + 1


# exercise 5
# while문을 이용하여 아래와 같이 별(*)을 표시하는 프로그램을 작성해 보자.
a=['*','*','*','*','*','*','*']
b=1
while b <= 4:
    print("".join(a[:]))
    a[b-1] = ' '
    a[-b] = ' '
    b = b + 1