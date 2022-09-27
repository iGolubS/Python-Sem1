# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число
# квадратом другого.
#     *Примеры:* 
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# if a*a==b:
#     print (f'- {a}, {b} -> да')

# elif b*b==a:
#     print (f'- {a}, {b} -> да')

# else:
#     print (f'- {a}, {b} -> нет')





# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# Решение 1:

# a = int (input('Введите число a: '))
# b = int (input('Введите число b: '))
# c = int (input('Введите число c: '))
# d = int (input('Введите число d: '))
# e = int (input('Введите число e: '))
# max1 = a      
# if b>max1:
#     max1 = b
# if c>max1:
#     max1 = c
# if d>max1:
#     max1 = d
# if e>max1:
#     max1 = e
# print(max1)


# Решение 2:

# numbers = int(input(' input amount of numbers:  '))
# count = 1
# arr = []
# while( count <= numbers):
#     num = int(input(f"input {count} number: "))
#     arr.append(num)
#     count += 1 
# print (arr)
# max_num = arr[0]
# for i in arr:
#     if i > max_num:
#         max_num = i

# print(f' max number is: {max_num}')


# Решение 3:

# a = int (input("введите a: "))
# b = int (input("введите b: "))
# c = int (input("введите c: "))
# d = int (input("введите d: "))
# e = int (input("введите e: "))

# m = a
# for i in b,c,d,e:
#     if i>m: m=i
# print(m)





# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#     *Примеры:* 
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# Решение 1:

# n = int(input("Введите число N= "))
# m = range(-n, n+1, 1)
# for i in m:
#     print(i)


# Решение 2:

# print('введите числа')
# value = int(input())
# n = value*(-1)
# print (list (range(-value, value)))




# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

n = float(input('Введите n: '))
print(int(n * 10  % 10))