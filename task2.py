#Найдите сумму цифр трехзначного числа.

n = int(input("Введите число: "))

a = n // 100
print (a)
b = n // 10 % 10
print (b)
c = n % 10
print (c)

print (f'Сумма = {a + b + c}')