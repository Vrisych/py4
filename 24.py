n= int(input("Введите число кустов: " ))
arr = list()
print('Введите число ягод на каждом кусте')
for i in range(n):
    arr.append(int(input()))
max=0
for k in range(n-1):
    check = arr[k-2]+arr[k-1]+arr[k]
    if check>max: max = check
print(f"Максимальное число ягод, которое можно собрать равно {max}")