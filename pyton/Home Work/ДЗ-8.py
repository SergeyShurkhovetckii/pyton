################################
#1
#написать программу которая находит числа у которых 5 делителей
# и вывести 2 максимальных делителя
# числа на промежутке от 1000 до 50000


# def action ():
#     integers = []
#     for i in range (1000 , 50000):
#         if i % 5 == 0 :
#             integers.append(i)
#     # return (integers[: -2])
#     # return (integers.sorted(max))
#     return max(integers)
# # Как получить 2 хз
# a = action()
# print(a)

################################
#2
# НАЧАЛО
# ПОКА нашлось(АА) ИЛИ нашлось(ВВ) ИЛИ нашлось(АВ)
#   заменить(АА, В)
#   заменить(ВВ, А)
#   заменить(АВ, ВА)
# КОНЕЦ ПОКА
# КОНЕЦ
# Известно, что на вход программы поступила строка из 52 подряд идущих комбинаций «АВ»


# a = 'AB' * 52
# print(a)
#
# while 'AA' in a or 'BB' in a or 'AB' in a :
#     if 'AA' in a :
#         a=a.replace('AA', 'B',1)
#     if 'BB' in a :
#         a=a.replace('BB', 'A',1)
#     if 'AB' in a :
#         a=a.replace('AB','BA',1)
#
# print(a)

##################################
#3
# НАЧАЛО
# ПОКА нашлось(11)
#   заменить(112, 4)
#   заменить(113, 2)
#   заменить(42, 3)
#   заменить(43, 1)
# КОНЕЦ ПОКА
# КОНЕЦ
# Какая строка получится в результате применения приведённой программы
# к строке вида 1…13…32…2, состоящей из 170 единиц, 100 троек и 7 двоек?


s = '1' * 170 , '3' * 100 , '2'*7
print(s)

while '11' in s :
    if '112' in s :
        s=s. replase ('112','4' ,1)
    if '113' in s :
        s=s.replase ('113','2' ,1)
    if '42' in s :
        s=s.replase ('42','3' ,1)
    if '43' in s:
        s=s.replase ('43','1',1)

print(s)


#####################################
#4

