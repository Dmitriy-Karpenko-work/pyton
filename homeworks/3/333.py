# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3
# -> 1
'''
len_list = input("Введите кочичество элементов в списке:[от 1 до ...] ")  # A[1..N]
test_list = input("Введите элементы списка через пробел ").split()
f_num = input("Введите число которое ищите ")
count= 0
for i in range(len(test_list)):
    if f_num == test_list[i]:
        count+=1
    else:
        i+=1    
print(f'Число {f_num} встречается в списке {count} раз')

'''
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример: *

# 5
# 1 2 3 4 5
# 6
# -> 5


'''
len_list = 5 #input("Введите кочичество элементов в списке:[от 1 до ...] ")  # A[1..N]
test_list = [1,76,45,56,7] #input("Введите элементы списка через пробел ").split()
sorted_list = sorted(test_list)
f_num =  40#input("Введите число которое ищите ")

para0 = 0
para1 = 0
res = 0
print(sorted(test_list))
# ---------------------------------------------------------------------------------------------------------------
#НЕ РАБОТАЕТ
if f_num > sorted_list[-1]: 
    print('------ближайшее число-[-1]-------') # если искомое число больше последнего элемента то ближайшее число последний элемент
    print(sorted_list[-1])
elif f_num < sorted_list[0]:
    print('------ближайшее число-[1]----') # если искомое число меньше второго то ближайшее число 1
    print(sorted_list[0])
     # 43
# наше число между двумя элементами

for i in range(len(sorted_list)):
        #       [1,                     7,      45, 56, 76]
        #       1           6               46
        if sorted_list[i] < f_num < sorted_list[i+1]:
            count_0 = sorted_list[i]-f_num # -33
            count_1 = sorted_list[i+1]-f_num #5
            if count_0 > count_1:
                print(f'ближайшее число 1 {sorted_list[i]}')
                break
            elif count_0 < count_1:
                print(f'ближайшее число 2 {sorted_list[i+1]}')
                break
                
#---------------------------------------------------------------------------------------------------------------
#НЕ РАБОТАЕТ
for i in range(len_list-1):
    para0 = sorted_list[i]-f_num
    para1 = sorted_list[i+1]-f_num
    print(para0, para1)
    if para0 > para1:
        print(sorted_list[i])
    elif para0 == para1:
        print(sorted_list[i])
    elif para0 < para1:
        print(sorted_list[i])
        print()
#---------------------------------------------------------------------------------------------------------------
#НЕ РАБОТАЕТ
len_list = 5 #input("Введите кочичество элементов в списке:[от 1 до ...] ")  # A[1..N]
test_list = [1,76,45,56,7] #input("Введите элементы списка через пробел ").split()
sorted_list = sorted(test_list)
f_num =  40#input("Введите число которое ищите ")
print(sorted_list)
number = 0
for i in range(len(sorted_list)):
    print(sorted_list)
    if (f_num-sorted_list[i]) < f_num-number and f_num-sorted_list[i] > 0:
        number = i
print(sorted_list[number])
#---------------------------------------------------------------------------------------------------------------
'''

# *Задача 20: * В настольной игре Скрабл(Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так: 
# A, E, I, O, U, L, N, S, T, R – 1 очко
# D, G – 2 очка
# B, C, M, P – 3 очка
# F, H, V, W, Y – 4 очка
# K – 5 очков
# J, X – 8 очков
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко
# Д, К, Л, М, П, У – 2 очка
# Б, Г, Ё, Ь, Я – 3 очка
# Й, Ы – 4 очка
# Ж, З, Х, Ц, Ч – 5 очков
# Ш, Э, Ю – 8 очков
# Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Версия 1 "работает и ладно" ---------------------------------------------------------------------------------------------------------

'''
word_origin = ((input("Введите слово (Ru/Eng): ")))
print(str(word_origin).upper())
up_word = (word_origin).upper()

word_next = (list(up_word))
print((list(up_word)))
print(word_next[0])
point = int()
for i in range(len(word_origin)):
                                                                                                                                                                                                                                                             
    if word_next[i] == "А" or word_next[i] == "В" or word_next[i] == "E" or word_next[i] == "И" or word_next[i] == "Н" or word_next[i] == "О" or word_next[i] == "Р" or word_next[i] == "С" or word_next[i] == "Т" or word_next[i] == "A" or word_next[i] == "E" or word_next[i] == "I" or word_next[i] == "O" or word_next[i] == "U" or word_next[i] == "L" or word_next[i] == "S" or word_next[i] == "T" or word_next[i] == "R":
        point = point+1
    elif word_next[i] == "Д" or word_next[i] == "К" or word_next[i] == "Л" or word_next[i] == "М" or word_next[i] == "У" or word_next[i] == "П" or word_next[i] == "D" or word_next[i] == "G":
        point += 2
    elif word_next[i] == "Б" or word_next[i] == "Г" or word_next[i] == "Ё" or word_next[i] == "Ь" or word_next[i] == "Я" or word_next[i] == "P" or word_next[i] == "M" or word_next[i] == "C" or word_next[i] == "B":
        point += 3                                                                       
    elif word_next[i] == "Й" or word_next[i] == "Ы" or word_next[i] == "F" or word_next[i] == "H" or word_next[i] == "V" or word_next[i] == "W" or word_next[i] == "Y":
        point += 4
    elif word_next[i] == "Ж" or word_next[i] == "З" or word_next[i] == "Х" or word_next[i] == "Ц" or word_next[i] == "Ч" or word_next[i] == "K":
        point += 5   
    elif word_next[i] == "Ш" or word_next[i] == "Э" or word_next[i] == "Ю" or word_next[i] == "J" or word_next[i] == "X":
        point += 8
    elif word_next[i] == "Ф" or word_next[i] == "Щ" or word_next[i] == "Ъ" or word_next[i] == "Q" or word_next[i] == "Z":
        point += 10
    print(word_next[i] ,point)
print(word_origin, point)
'''

#Версия 2 "оптимизирована для чтения" ---------------------------------------------------------------------------------------------------------
'''
word_origin = ((input("Введите слово (Ru/Eng): ")))
print(str(word_origin).upper())
up_word = (word_origin).upper()

word_next = (list(up_word))
print((list(up_word)))
print(word_next[0])
point = int()
# ['Н', 'О', 'У', 'Т', 'Б', 'У', 'К']
for i in range(len(word_origin)):
    
    if word_next[i] in ('А,В, Е, И, Н, О, Р, С, Т,      A, E, I, O, U, L, N, S, T, R'):
        point = point+1
        print(word_next[i], point)
    elif word_next[i] in ('Д, К, Л, М, П, У,            D, G'):
        point += 2
    elif word_next[i] in ('Б, Г, Ё, Ь, Я,               B, C, M, P '):
        point += 3
    elif word_next[i] in ('Й, Ы,                        F, H, V, W, Y'):
        point += 4
    elif word_next[i] in ('Ж, З, Х, Ц, Ч,               K'):
        point += 5
    elif word_next[i] in ('Ш, Э, Ю,                     J, X'):
        point += 8
    elif word_next[i] in ('Ф, Щ, Ъ,                     Q, Z'):
        point += 10
    print(word_next[i], point)
print(word_origin, point)
'''

# Версия 3 "словари" ---------------------------------------------------------------------------------------------------------
'''
word_origin = ((input("Введите слово (Ru/Eng): ")))
up_word = (word_origin).upper()
print((list(up_word)))
word_next = (list(up_word))
#----------------------------------------------
list_letters = {1: "AEIOULNSTRАВЕИНОРСТ",           
                2: "DGДКЛМПУ",
                3: "BCMPБГЁЬЯ",
                4: "FHVWYЙЫ",
                5: "KЖЗХЦЧ",
                8: "JXШЭЮ",
                10: "QZФЩЪ"}
#----------------------------------------------

point = 0
for i in word_next:                         # цикл на длину слова
                                            #print(i)
    for key, val in list_letters.items(): #читаем ключи и хранилища .item()
                                            #print(i,key,val)
        if i in val:                        #если буква в хранищище ТО
            point += key                    # ТО мы прибовляем key а если нет то это выход за условия задачи
print(f"количестово очков: {point}")
'''

#.items() - запоминить Прочитали положили обратно






'''
------------------------------------------------------------------------------
первая версия словаря
slovar = {
    # key:value
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'D': 2, 'G': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'Й': 4, 'Ы': 4,'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,'K': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,'J': 8, 'X': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10,'Q': 10, 'Z': 10}
'''