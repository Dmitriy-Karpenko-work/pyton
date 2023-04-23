# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
test_list = ("a a a b c a a d c d d").split()
print(type(test_list))
slovar={}
for i in test_list:
    if i in slovar:
        print(f'{i}_{slovar[i]}')
        slovar[i] += 1
    else:
        print(f'{i}')
        slovar[i]=1
