# Задайте список из нескольких чисел. 
# напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

def sum_odd(array):
    sm = 0
    for i in range(len(array)):
        if i%2: sm += array[i]
    return sm

arr = list(map(int, input('Введите список ').split()))
print(sum_odd(arr))