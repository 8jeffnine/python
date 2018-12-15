money = 1
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

x = 3
y = 2
print(x>y)
# True
print(x<y)
# False
print(x==y)
# False
print(x!=y)
# True

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
# ==> 걸어가라


money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
# ==> 택시를 타고 가라

print(1 in [1, 2, 3])
# ==> True
print(1 not in [1, 2, 3])
# ==> False

print('a' in ('a', 'b', 'c'))
# ==> True
print('j' not in 'python')
# ==> True

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
# ==> 택시를 타고 가라

pocket = ['paper', 'handphone']
card = 1
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")
# ==> 택시를 타고 가라

pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")
# ==> 택시를 타고 가라

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")
# ==> '' (pass)


## 파이썬의 조건부 표현식(conditional expression)
# score가 60이상인 경우 message가 success, 아닐경우 failure
score = 60
message = "success" if score >= 60 else "failure"
print(message)

score = 59
message = "success" if score >= 60 else "failure"
print(message)


# exercise 1
money = 5000
card = False
if money >= 4000:
    print('Taxi')
elif card:
    print('Taxi')
else:
    print('not Taxi')


# exercise 2
lucky_list = [1, 9, 23, 46]
hong = 23
if hong in lucky_list:
    print('야호')

# exercise 3
input = 1
if input%2 == 0:
    print('짝수')
else:
    print('홀수')

# exercise 4
# 다음 문자열을 분석하여 나이가 30미만이고 키가 175이상인 경우에는 YES를 출력하고 아닌 경우에는 NO를 출력하는 프로그램을 작성하시오.
a = {'나이':30,'키':180}
if a.get('나이') < 30 and a.get('키') >=175:
    print('YES')
else:
    print('NO')

# exercise 5
a = "Life is too short, you need python"
if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')
# ==> shirt