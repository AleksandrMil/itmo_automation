a = 3
b = 4
if a > b:
    print(a)
else:
    print(b)

q = -10
w = 125
if abs(q-w)==135:
    print('YES')
else:
    print('NO')

m = 1
if m==1 or m==2 or m==12:
    print('Зима')
elif 3 <= m <= 5:
    print('Весна')
elif 6 <= m <= 8:
    print('Лето')
elif 9 <= m <= 11:
    print('Осень')


x = 11
y = 22
p = 33
if x >10 and y > 10 and p > 10:
    print('YES')
else:
    print('NO')

sp = [1, 2, 3, 4, 5]
n = 0
for i in sp:
    if i % 2 == 0:
        n+=1
print(n)

years = 3
months = 8
days=29*(months+years*12)
print(days)
