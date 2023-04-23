count_wat = int(input('--> '))

min_wat = int(input('water_1: '))
max_wat = min_wat

for i in range(count_wat - 1):
    wat = int(input(f'water_{i + 2}: '))
    if wat > max_wat:
        max_wat = wat
    elif wat < min_wat:
        min_wat = wat

print(min_wat, max_wat)
