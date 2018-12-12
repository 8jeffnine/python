dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)

a = {1: 'hi'}
print(a)

a = { 'a': [1,2,3]}
print(a)

# dic, add pair of dic
a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

# dic, remove pair of dic
del a[1]
print(a)

# dic, get value using key
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])


a = {1:'a', 2:'b'}
print(a[1])
print(a[2])

a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

# waring, duplicated key value is ignored
a = {1:'a', 1:'b'}
print(a[1])


# dic, list of keys
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())

for k in a.keys():
    print(k)

print(list(a.keys()))

# dic, list of values
print(a.values())

# dic, pair list of key, value
print(a.items())

# dic, clear of key, value pair
print(a.clear())

# dic, get value using key
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))

# dic, checking.. key is exist in dic
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
print('email' in a)


# exercise 1
a={'name':'홍길동','birth':'1128','age':30}
print(a)

# exercise 2


# exercise 3
# 딕셔너리 a에서 'B'에 해당되는 값을 추출하고 삭제해 보자.
a = {'A':90, 'B':80, 'C':70}
print(a.get('B'))
del a['B']
print(a)


# exercise 4
# function : get(find_value,default_return_value)
a = {'A':90, 'B':80}
print(a.get('C',70))

# exercise 5
a = {'A':90, 'B':80, 'C':70}
print(min(a.values()))

# exercise 6
# {'A':90, 'B':80, 'C':70} ==> [('A', 90), ('B', 80), ('C', 70)]
a = {'A':90, 'B':80, 'C':70}
print(a.items())