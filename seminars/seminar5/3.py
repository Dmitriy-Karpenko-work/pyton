# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)


# Input: 5

# Output: yes




def prostoe_proverka(num):
    # if num in (1,0):
    #     return False
    
    for i in range(2,(num // 2)+1):
        if (num % i ==0):
            return False
    return True    

N = int(input("Введите число: "))
print(prostoe_proverka(N))
