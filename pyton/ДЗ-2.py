#########################################
#1
x = int(input("Введите число"))

if x % 2 ==0:
    print(x/2)
else :
    print(x%2)
   # print("Число делиться с остатком Остаток{0}" .format(x==x%2))
if x % 3 ==0:
    print(x/3)
else :
    print(x%3)
    
if x % 7 ==0:
    print(x/7)
else :
    print(x%3)
    

#########################################
#2
name = input('Введите имя')
password = input('Введите пароль')

if name=='Sergey'and password=='12345':
 print('{name}Вход одобрен'.format(name=name,password=password))
 
else:
    print('Вход запрещен данные не верные ')

###################################
#3
x = int(input('Введите 3 числа'))
y = int(input())
z = int(input())

if x > y or x > z :
    print ('Самое большое число x')
    
elif y > x or y > z :
    print ('Самое большое число y')
    
elif z > x or z > y :
    print ('Самое большое число z')   


########################################
#4
name = input('Как вас зовут')
age = int(input('Введите ваш возвраст'))
sport = input('Каким спортом вы любите заниматься')
food = input('Какое ваше любимое блюдо')

    
print('Меня зовут{0}, Мой возвраст {1}, Мой любимый спорт {2}, Мое любимое блюдо{3}'.format(name,age,sport,food))

#########################################