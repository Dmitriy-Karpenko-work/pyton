
'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
'''
#!!!элементы множеств - это Объекты, входящие в множество, называются элементами этого множества.

# объявление первого списка
test_list1 = [9, 8, 7, 1, 2, 3, 9, 8, 7, 1, 2, 3,10,3221 ,2123 ,11,23,4322,48]
sorted_test_list1 = set(sorted(test_list1))
print(f'список 1{sorted_test_list1}')
# объявление второго списка
test_list2 = [4, 6, 5, 7, 3, 1, 4, 6, 5, 7, 3, 1,56,47,45,69,87,21,35,689,47]
sorted_test_list2 = set(sorted(test_list2))
print(f'список 2{sorted_test_list2}')
'''
n = int(input('кол-во элементов первого множества' ))
m = int(input('кол-во элементов второго множества' ))
'''
# объявление чмсел которые нам нужны
find = input('Введите элементы множеств ').split()
sorted_find = (sorted((find)))
print(sorted_find)

#--------------решение---------------

testlist3 = []
testlist3 = (sorted_test_list1.intersection(sorted_test_list2))
print(testlist3)





# .intersection - как union только наоборот (соединяет только повторяющиеся)



'''
эталонное решение не понятно них,,,
#
mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')
'''


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.



[0,1,2,3,4,5]
[1,2,3,4,5,6]