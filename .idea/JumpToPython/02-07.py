a = True
b = False

print(1 == 1)
print(2 > 1)
print(2 < 1)

a = [1, 2, 3, 4]
while a:
    print(a.pop())


if []:
    print("참")
else:
    print("거짓")


if [1,2,3]:
    print("참")
else:
    print("거짓")


print(bool('python'))
print(bool(''))

print(bool([1,2,3]))
print(bool([]))
print(bool(0))
print(bool(3))


# exercise 1
# 다음은 불 자료형을 리턴하는 조건문들이다. 각 각의 예제의 결과가 어떻게 나오는지 예상해 보자.
print( 1 != 1 )
# => false
print( 3 > 1 )
# => true
print( 'a' in 'abc' )
# => true
print( 'a' not in [1, 2, 3] )
# => true

# exercise 2
# bool 연산자를 이용하여 다음 자료형들의 참과 거짓을 판별하시오.
a = "python"
b = ""
c = (1,2,3)
d = 0

print(bool(a))
# => true
print(bool(b))
# => false
print(bool(c))
# => true
print(bool(d))
# => false