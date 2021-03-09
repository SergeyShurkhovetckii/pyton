###################
# #1
# def action ():
#     for i in range(1 ,end):
#         print(i )


# end = int(input("Введите диопазон"))


# action ()

#########################
#2
# def action():
#     for i in a :
#         if i =='ф' or i == 'б' or i == 'ч':
#             print(i)


# a = 'фибоначчи'

# action()

################################
#3

# def action ():
#     print("привет", first_name ,last_name ,"твой пол", sex )


# first_name = input("Введите свое имя")
# last_name = input("Введите свою фамилию")
# sex = input ("Введите свой пол")


# action()
#################################
#4

# def numb():
#     i = a + b +c
#     i = i / 3 
#     print(i)
   
# a = int(input("Введите число1 "))
# b = int(input("Введите число2 "))
# c= int(input("Введите число3 "))

# numb ()

###################################
#5

# def numb ():
#     i = a + b + c
#     i = i % 3 == 0 
#     print(i%3) 



# a = int(input("Введите число1 "))
# b = int(input("Введите число2 "))
# c= int(input("Введите число3 "))


# numb()


###################################
#6
# def numb():
#     if a % 2 == 0 :
#         print("Число четное ")
    
#     else:
#         print("Число не четное")


# a = int(input("Введите число"))


# numb()

##################################
#7
def action(a,b,c):
    discriminant = b**2 - 4*a*c
    print("Дискриминант равен {}".format(discriminant))
    if discriminant < 0:
	    print("Корней нет")


    if 	discriminant > 0:
        x1  = (-b + math.sqrt(discriminant)) / ( 2 * a)
        x2  = (-b - math.sqrt(discriminant)) / ( 2 * a)
        print("Ввыводим{x}".format (x=x1))
        print("Ввыводим{x2}".format (x2=x2))

    if  discriminant == 0:
        x = -b / ( 2 * a)
        print("Ввыводим x {} ".format(x))


a = int(input('Веедите a'))
b = int(input('Веедите b'))
c = int(input('Веедите c'))


action(a,b,c)







