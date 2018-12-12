odd = [1, 3, 5, 7, 9]

a = [ ]
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

print(a)
print(b)
print(c)
print(d)
print(e)

a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2])
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])

print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])

a = [1, 2, 3, 4, 5]
print(a[0:2])

a = "12345"
print(a[0:2])

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]

print(b)
print(c)

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

# add List
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

# multiply List (Repeat)
a = [1, 2, 3]
print(a*3)

a = [1, 2, 3]
# a[2]+"hi" => 3hi (x)
print(str(a[2])+"hi"+" ==> (0)")

# modify one of list value
a = [1, 2, 3]
a[2] = 4
print(a)

# modify range of list value
print(a[1:2])
a[1:2] = ['a', 'b', 'c']
print(a)

# a[1] != a[1:2]
a[1] = ['a', 'b', 'c']
print(a)

# delete using []
a[1:3] = [ ]
print(a)

# delete using 'del' function
del a[0]
print(a)

# List add value using 'append'
a=[1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)

# List sorting
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)

# List reverse
a = ['a', 'c', 'b']
a.reverse()
print(a)

# return location value ==> index(find_value)
a = [1,2,3]
print(a.index(3))
print(a.index(1))

# Error : find value is not exist in list
# print(a.index(0))

# List, Insert
a = [1, 2, 3]
a.insert(0,4)
print(a)

a.insert(3, 5)
print(a)

# List, remove ==> remove(find_value<first find>)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

# List, pop() ==> remove last value of List
a = [1,2,3]
a.pop()
print(a)

# List, pop(index_value) ==> return and remove value which has index of list
a = [1,2,3]
a.pop(1)
print(a)

# List, count(find_value) ==> return count of find_value in list
a = [1,2,3,1]
print(a.count(1))

# List, extend ==> a.extend(b) mean b list add to a list
a = [1,2,3]
a.extend([4,5])
print(a)

b = [6, 7]
a.extend(b)
print(a)


# remove using find_value ==> remove(value)
# remove using index of list ==> pop(index)


# exercise 1
a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
print(a[4] + " " + a[2])

# exercise 2
a = ['Life', 'is', 'too', 'short']
print(" ".join(a[:]))

# exercise 3
a = [1, 2, 3]
print(len(a))

# exercise 4
a = [1, 2, 3]
a.append([4,5])
print("append : ")
print(a)

a = [1, 2, 3]
a.extend([4,5])
print("extend : ")
print(a)

# exercise 5
# [1, 3, 5, 4, 2]라는 리스트를 [5, 4, 3, 2, 1]로 만들어보자.
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# exercise 6
# [1, 2, 3, 4, 5]라는 리스트를 [1, 3, 5]로 만들어 보자.
a = [1, 2, 3, 4, 5]
a.pop(3)
a.pop(1)
print(a)

# a.remove(2)
# a.remove(4)
# print(a)



