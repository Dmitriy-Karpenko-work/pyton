# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример: *

# 5
# 1 2 3 4 5
# 6
# -> 5



len_list = 6 #input("Введите кочичество элементов в списке:[от 1 до ...] ")  # A[1..N]
test_list = set([1,45,76,45,56,7]) #input("Введите элементы списка через пробел ").split()
sorted_list = sorted(test_list)
f_num =   54 #input("Введите число которое ищите ") # Введите число которое ищите


count_1 = 0
count_0 = 0
break_out_flag = False
print(sorted(test_list))
# --------------------------работает))))))))))))))
if f_num > sorted_list[-1]: 
    print('------ближайшее число-[-1]-------') # если искомое число больше последнего элемента то ближайшее число последний элемент
    print(sorted_list[-1])
elif f_num < sorted_list[0]:
    print('------ближайшее число-[1]----') # если искомое число меньше первого числа то ближайшее число 1
    print(sorted_list[0])
else:
    for i in range(len(sorted_list)):
        if count_0 > count_1:  # проверка первое число больше второга число
            print(f"ближайшее число {sorted_list[i-1]}")
            break_out_flag = True
            break
        if i == len_list-1: #проверка чтобы не выходить за рамки списка
            break_out_flag = True
            break
        else:# основное действие:берем числа по счету один и два
            count_0 = sorted_list[i]  # число один
            count_1 = sorted_list[i+1]  # число два
        print(count_0, count_1) #
        print("-----------------")
        count_0 = (sorted_list[i]-f_num)  # первое число всегда меньше второга
        count_1 = (sorted_list[i+1]-f_num)*-1  # второе число умножаем на -1
        print(count_0, count_1)
        print("-----------------")


