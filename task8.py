# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

n = int(input('n (длина)= '))
m = int(input('m (ширина)= '))

k = int(input('Сколько долек надо отломить: '))

if k % n == 0 or k % m == 0:
    print('да, получится разломить шоколадку на два прямоугольника')
else:
    print('нет, не получится разломить шоколадку на два прямоугольника')