x = int(input('Введите значение X: '))
y = int(input('Введите значение Y: '))
if x > 0 and y > 0:
    print('Первая четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x < 0 and y > 0:
    print('Вторая четверть') 