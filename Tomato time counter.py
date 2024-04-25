minutes_in_tomato, minutes_in_short_break, minutes_in_long_break = 25, 5, 15
print('Введите кол-во томатов или "0", чтобы выйти.')
for inp in iter(lambda: int(input('>>> ')), 0):
    minutes = inp * minutes_in_tomato + \
              (inp - 1) * minutes_in_short_break + \
              ((inp - 1) // 4) * (minutes_in_long_break - minutes_in_short_break)
    hours = str(minutes // 60)
    if len(hours) > 1 and hours[-2:] in ('11', '12', '13', '14'):
        print('Понадобится', hours, 'часов и', minutes % 60, 'минут!')
    elif hours[-1] == '1':
        print('Понадобится', hours, 'час и', minutes % 60, 'минут!')
    elif hours[-1] in ['2', '3', '4']:
        print('Понадобится', hours, 'часа и', minutes % 60, 'минут!')
    else:
        print('Понадобится', hours, 'часов и', minutes % 60, 'минут!')
