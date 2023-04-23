
arr = [0, -1, 5, 6, 1,7]
count = 0
for i in range(len(arr)):
    print(f'{arr[i]}>{arr[i-1]}')
    if arr[i] > arr[i-1]:
            count += 1
            print(f'{arr[i]}>{arr[i-1]}    ++да++')
    else:
            print(f'{arr[i]}>{arr[i-1]}    --нет--')
print (count)
