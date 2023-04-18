# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


numbers = [1, 2, 3, 4, 30]

# Вариант [1] - Modified создаем доп массив
list_result = []
len_list = len(numbers)
for i in range(len_list - k, len_list):  
# так как число сдвига (к) это и есть пос ути число последних цифр массива
#  то есть массив (1, 2, 3, 4 ,5) если двинуть на 3 элемента, то будет массив (3, 4, 5, 1, 2 )
    list_result.append(numbers[i])
for i in range(len_list - k):
    list_result.append(numbers[i])
print(list_result)

# Вариант 2
# list_result = []
# for i in range(len(numbers)):
#     list_result.append(numbers[-k + i])
# print(list_result)

# Вариант 3 - Original - рабобаем с исходным массивом
for _ in range(k):
    numbers.insert(0, numbers.pop())
print(numbers)


# Вариант 4 - так как исходный список поменял, создадим его ещё раз
numbers = [5, 4, 6, 7, 8, -10]
print(numbers[-k:] + numbers[:-k])