# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример: *
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# ---------------------СПОСОБ 1 Арифметический--------------------
# num = int(input("Введите число: "))

# num1 = num //100
# num2 = (num//10)%10
# num3 = num % 10
# num_res = num1+num2+num3
# print(f"{num_res} ---> {num1}+{num2}+{num3}")
# #---------------------СПОСОБ 2 Вырываем из строки-------------
# num = (input("Введите число: "))
# num1 = int(num[0])
# num2 = int(num[1])
# num3 = int(num[2])
# num_res = num1+num2+num3
# print(f"{num_res} ---> {num1}+{num2}+{num3}")
# -------------------------------------------------------------


# # Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# # Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# # а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# # *Пример: *

# # 6 -> 1  4  1
# # 24 -> 4  16  4
# # 60 -> 10  40  10

# Sum = input("Введите число журавликов: ")
# Petya = int(Sum/3/2)
# Sergey = int(Sum/3/2)
# Kate = (Petya+Sergey)*2
# print(f"{Petya} {Kate} {Sergey}")


# --------------------------------------------------------------------------------------------------------------------------------------------

# # Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# #  вы расплачивались за проезд и получали билет с номером.
# #  Счастливым билетом называют такой билет с шестизначным номером,
# #  где сумма первых трех цифр равна сумме последних трех.
# # Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5 = 9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# # *Пример: *

# # 385916 -> yes
# # 123456 -> no


# num = (input("Введите число: "))
# num1 = int(num[0])
# num2 = int(num[1])
# num3 = int(num[2])
# num4 = int(num[3])
# num5 = int(num[4])
# num6 = int(num[5])
# if (num1+num2+num3 == num4+num5+num6):
#     print ("yes")
# else:
#     print("no")

# --------------------------------------------------------------------------------------------------------------------------------------------

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#  если разрешается сделать один разлом по прямой между дольками(то есть разломить шоколадку на два прямоугольника).

# *Пример: *

# 3 2 4 -> yes
# 3 2 1 -> no

# length = int(input("Введите длину шоколада: "))
# width = int(input("Введите ширину шоколада: "))
# dolki = int(input("Введите кол-во долек: "))
# if (length*width >dolki):
#    if (dolki % length == 0 or dolki % width == 0):
#         print("yes")
#    else:
#       print("no")
# else:
#     print("no")


