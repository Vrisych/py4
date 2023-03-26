n= int(input("Введите количество элементов первого множества: "))
m= int(input("Введите количество элементов второго множества: "))
set1=set()
set2=set()
print("Введите элементы первого множества")
for i in range(n):
    set1.add(int(input()))
print("Введите элементы второго множества")
for i in range(m):
    set2.add(int(input()))
order = list(set1.intersection(set2))
order.sort()
print (f"Повторяющиеся числа: {order}")