print("Hello World")
print('python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')

food="Python's favorite food is perl"
print(food)
heSay='"Python is very easy." he says.'
print(heSay)
multiLine='Life is very short.\nYou need python'
print(multiLine)
multiLine='''
Life is too short
You need python
'''
print(multiLine)
head="Python"
tail=" is fun!"
print(head+tail)
a="python"
print(a*2)
print("="*50)
print("My Program")
print("="*50)
a = "Life is too short, You need Python"
print(a[3])

print(a[0])
print(a[12])
print(a[-1])

print(a[-0])
print(a[-2])
print(a[-5])
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
print(a[0:3])
print(a[0:5])

print(a[0:2])
print(a[5:7])
print(a[12:17])
print(a[19:])
print(a[:17])
print(a[19:-7])

a = "20010331Rainy"
year=a[:4]
day=a[4:8]
weather=a[8:]
print(year)
print(day)
print(weather)

a = "Pithon"
print(a[1])
# a[1]='y' // immutable data-type. thus i can't change letter
# print(a[1])

print(a[:1]+'y'+a[2:])

# format 함수를 이용한 포매팅
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
print("I eat %d apples." % number)

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

# 정렬(좌/우/가운데/빈칸채우기)
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

# { 또는 } 문자 표현하기
print("{{ and }}".format())

# f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

print(f'{y:0.4f}')
print(f'{y:10.4f}')
print(f'{{ and }}')

# 문자열 관련 함수들
a = "hobby"
print(a.count('b'))

# find는 찾는 문자열이 없을 경우 -1
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

# index는 찾는 문자열이 없을 경우 error
a = "Life is too short"
print(a.index('t'))
# print(a.index('k'))

# 문자열 삽입(join)
a= ","
print(a.join('abcd'))
print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))

# 대/소문자 전환
a = "hi"
print(a.upper())

a = "HI"
print(a.lower())

a = " hi "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# 문자열 치환(replace)
a = "Life is too short"
print(a.replace("Life","Your leg"))
print(a.split())

a = "a:b:c:d"
print(a.split(":"))


# 문제1
print("점프 투 파이썬")

# 문제2
print("Life is too short\nYou need Python")

# 문제3
print("{0:>30}".format("PYTHON"))

# 문제4
print("881120-1068234".split('-'))

# 문제5
pin = "881120-1068234"
print(pin[7])

# 문제6
a="1980M1120"
print("M%s" % "".join(a.split('M')))

# 문제7
b="Life is too short, you need python"
print(b.index("short"))

# 문제8
c="a:b:c:d"
print(c.replace(":","#"))

# 문제9
d="a:b:c:d"
print("#".join(d.split(':')))