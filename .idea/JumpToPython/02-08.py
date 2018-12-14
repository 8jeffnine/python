# id(value) : 메모리의 주소
a=[1,2,3]
print(id(a))

b = a
print(id(a))
print(id(b))

print(a is b)

a[1] = 4
print(a)

a = [1, 2, 3]
b = a[:]

a[1]=4
print(a)
print(b)

from copy import copy
b = copy(a)
print(a)
print(b)
print(b is a)

a, b = ('python', 'life')
print(a)
print(b)

(a, b) = 'python', 'life'
print(a)
print(b)
print((a, b))

[a,b] = ['python', 'life']
print(a)
print(b)

a = b = 'python'
print(a)
print(b)

a = 3
b = 5
a, b = b, a
print(a)
print(b)


# exercise 1
#
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
# ==> False


# exercise 2
a = [1, 2, 3]
b = a
print(a is b)
# ==> True


# exercise 3
a = b = [1, 2, 3]
a[1] = 4
print(b)
# b=[1,4,3]


# exercise 4
a = [1, 2, 3]
b = a[:]
print(a is b)
# ==> False


# exercise 5
a = [1, 2, 3]
b = a[:]

a[1] = 4
print(a)
print(b)
# ==> b=[1,2,3]


# exercise 6
# + 기호를 이용하여 더한것과 extend한 것의 차이점?
a = [1, 2, 3]
a = [1, 2, 3]
a = a + [4,5]
print(a)

a = [1, 2, 3]
a.extend([4, 5])
print(a)


# exercise
a = [1, [2, 3], 4]
b = a[:]
a[1][0] = 5
print(a)
print(b)
# ==> b=[1,[5,3],4] ???
print(a is b)
# ==> False