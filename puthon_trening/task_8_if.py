num = -3
if num >= 0:
    print('число больше или равно 0')
else:
    print('число отрицательное')

str_1 ='test'
str_2 = 'test1'
if str_1 in str_2:
    print('YES')
else:
    print('NO')

n = 3.4
if n>0:
    print('Положительное число')
elif n==0:
    print('Ноль')
else:
    print('Число отрицательное')

num = 1
pp = True
if num > 0 and pp:
    print('num - положительное число')
elif not pp:
    print('Печать запрещена')

k = 5
if 1 <= k <= 4:
    print('бакалавр')
elif 5 <= k <= 6:
    print('магистр')
elif 7 <= k <= 9:
    print('аспитрант')
else:
    print('Введите корректный год обучения')

w = -3350
if w > 100 or w < -100:
    print('-')
else:
    print('+')


