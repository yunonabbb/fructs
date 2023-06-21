numbers = []
for i in range(10):
    number = int(input("Введите число: "))
    numbers.append(number)

slice_2_to_8 = numbers[1:8]
print("Срез с 2 по 8 числа:", slice_2_to_8)


import random

size = int(input("Введите размер массива: "))
array = [random.randint(1, 10) for _ in range(size)]

min_index = array.index(min(array))
max_index = array.index(max(array))

slice_min_max = array[min_index:max_index+1]
print("Срез между минимальным и максимальным числом:", slice_min_max)


brands = input("Введите названия автомобильных марок через пробел: ")
brands_list = brands.split()

if "Хонда" in brands_list:
    print("Среди введенных марок есть лучшая - Хонда")
else:
    print("Среди введенных марок нет Хонды")


fruits = input("Введите названия фруктов через пробел: ")
fruits_list = fruits.split()

if "яблоко" in fruits_list:
    print("Среди введенных фруктов есть яблоко")
else:
    print("Среди введенных фруктов нет яблока")


numbers = []
for i in range(10):
    number = float(input("Введите число от 0.1 до 0.9: "))
    numbers.append(number)

result_numbers = [num for num in numbers if abs(num - 0.2) < 1e-6]
print("Числа, разница с 0.2 которых равна 0:", result_numbers)


import random

size = int(input("Введите размер массива: "))
array = [random.uniform(0.1, 9.9999) for _ in range(size)]

count_of_twos = 0
for number in array:
    count_of_twos += str(number).count('2')

print("Количество цифр 2 в любом разряде всех ячеек массива:", count_of_twos)











