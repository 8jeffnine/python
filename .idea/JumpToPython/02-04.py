t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

# Error, when removing tuple value
t1 = (1, 2, 'a', 'b')
# del t1[0]

# Error, when changing tuple value
t1 = (1, 2, 'a', 'b')
# t1[0] = 'c'

# indexing
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

# slicing
t1 = (1, 2, 'a', 'b')
print(t1[1:])

# tuple add
t2 = (3, 4)
print(t1 + t2)

# tuple multiply
print(t2 * 3)


# exercise 1
# 숫자 3만을 요소값으로 가지는 튜플을 작성하라.
a=(3,)
t1=(a*3)
print(t1)

# exercise 2
# 다음은 튜플 (1, 2, 3)을 (1, 4, 3)과 같이 변경하려고 시도했을 경우이다. 오류의 원인에 대해서 설명하시오
print("we can't change any value of tuple")

# exercise 3
# (1,2,3)이라는 튜플에 4라는 값을 추가하여 (1,2,3,4)처럼 만들어 출력해 보자.
t1=(1,2,3)
t2=(4,)
print(t1+t2)
