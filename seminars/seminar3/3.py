num = int(input('Введите первое число: '))   # ввод первого числа
max_num = num                             # признаем его max
while num != 0:                       # проверка числа на 0
    # в цикле пишем остальную последовательность пока не булет равен 0
    num = int(input('Введите число: '))
    if num > max_num:  # запоминаем самое большое число
        max_num = num
print(f'Максимальное число  последовательности: {max_num}')
