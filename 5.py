#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(num):
    if num == 0: return 0
    elif num in [1,2]: return 1
    return fib(num-1) + fib(num - 2)

def chain_fib(n):
    array_fib = []
    for i in range(-n, n+1):
        if i < 0: array_fib.append((-1)**(-i+1) * fib(-i))
        else: array_fib.append(fib(i))
    return array_fib


n = int(input('Введите число '))
print(chain_fib(n))