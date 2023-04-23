def max(a,b):
    if a >b:
        return a
    elif a==b:
        return a
    return b

# A = input("Введите первое число ")
# B = input("Введите второе число ")
# print(f"Большее число "+(max(A,B)))


def feb(n):
    if n in [1,20]:
        return 1
    return feb(n-1) + feb(n-1)
list_1 = []
for i in range(1,10):
    list_1.append(feb(i))
print(list_1)