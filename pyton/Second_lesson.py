# a = 2
# b = 3
# switcher = True

# print('Введите первое число')

# x = int(input())

# print('Введите второе число')

# y = int(input())

# print('Что сделать с числами')

# action = input()

# if action == 'умножение':
# 	print(x*y)

# if action =='плюс':
# 	print(x+y)

# if action == 'минус':
# 	print(x-y)

# if action == 'деление':
# 	print(x/y)


##################################
x = int(input('Введите 3 числа'))
y = int(input())
z = int(input())

if x<y<z or z<y<x :
	print('Среднее число y')
elif y<x<z or z<x<y :
	print('Среднее число x')	
else :
	print('Среднее число z')

####################################

# x = int(input('Введите 2 числа'))
# y = int(input())

# if x>0 and y>0:
# 	print('1плоскость')

# elif  x<0 and y>0:	
# 	print('2плоскость')

# elif x<0 and y<0:
# 	print('3плоскость')
# elif x>0 and y<0:
# 	print('4плоскость')

######################################

# a = int(input('Введите число'))

# if a % 2 ==0 :
# 	print('Число четное')

# else :
# 	print('Число не четное')

# #elif a % 2 !=0 :	 
# #	print('Число не четное')

#########################################
# y = int(input('Вводим число'))

# x = input('Что будем делать')

# if x=='байт':
# 	print('{y}килобайт={x}байт '.format(y=y, x=y*1024))

# elif x=='килобайт':
# 	print('{y}байт={x}килобайт'.format(y=y, x=y/1024))

#############################################

# a = [1,2,3,4,5]

# if len (a) > 2 :
# 	print('Лист большой',len(a))

# elif len(a) < 2 :
# 	print('лист{a}'.format(a=len(a)))	


#############################################
# a = int(input('Вводим 2  числа '))
# b = int(input())

# if a > b :
# 	print('а больше  b ')

# elif a<b :
# 	print('a меньше   b ')	
############################################
















'''
if switcher == True:
	switcher = False

elif switcher == False:
	switcher = True

print(switcher)
'''


'''
if a != b:
	print('Число a не равно числу b')

if a < b:
	print('Число а меньше b')

else:
	print('число a равно b ')

'''