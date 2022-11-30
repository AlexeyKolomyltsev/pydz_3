# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def multpl_array(array):
    mpl_array = []
    iterator = len(array)//2 + len(array)%2
    for i in range(iterator):
        mpl_array.append(array[i] * array[-i - 1])
    return mpl_array

arr = list(map(int, input('Введите список ').split()))
new_arr = multpl_array(arr)
print(new_arr)