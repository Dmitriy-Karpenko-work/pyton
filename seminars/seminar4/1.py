
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

arr = [1, 1, 2, 0, -1, 3, 4, 4]  # задан список
new_set = set(arr)
print(arr)
print(f'В заданном списке {len(new_set)} различных чисел')

print()
print(*arr)
print()
print(*(set(arr)))
print()
print(len(set(arr)))


