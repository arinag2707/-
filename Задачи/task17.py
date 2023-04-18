# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# numbers = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]

# # Вариант 2
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(len(result))


#  Вариант 2
# numbers = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
# for num in numbers:
#     while numbers.count(num) != 1:  while работае только когда истина
#         numbers.remove(num)
# print(numbers)

# print (*[1, 2, 3, 4], sep=",", end='!')