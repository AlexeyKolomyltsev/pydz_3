#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def decimal_bin(num):
    bin_num = ''
    while True:
        bin_num += str(num % 2)
        num //= 2
        if num < 2:
            bin_num += str(num)
            break
    return bin_num[::-1]

print(decimal_bin(20))
print(decimal_bin(100))
