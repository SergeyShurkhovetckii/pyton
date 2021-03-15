####################################
#1
# def action (a):
#     c = a + 100 * 5
#     print(c)

# a = 50 

# action(a)


#######################################
#2
# def hello():
#     print("hello World")

# hello()


#############################################
#3
# 0 1 1 2 3 5 8 13



# def fibonach(end):
    
#     fib1 = 1
#     fib2 = 1 

#     i = 0 
    
#     while i < end :
#         fibsome = fib1 + fib2
#         fib1 = fib2
#         fib2 = fibsome
#         i = i + 1 
#         print(fib2)

# end = int(input("До какого числа вывводить"))


# fibonach(end)





##############################################
#4


# a = 'Калькулятор'

# for i in a :
#     if i =='а':
#         print(i)


# def actinon(a):
#     for i in a :
#         # or i =='р':
#         if i =='а':
#             print(i)
#         if i =='р':
#             print(i)    
#         else :
#             print(i)  

# a = 'Калькулятор'

# actinon(a)



##############################################
#5
# def action (i,end):
#     if i <= end :
#         print(i)
#     else :
#         print("Число не входит в диапозон ")    

# end = 10 
# i = int(input("Введите число из диопазона "))


# action (i,end)

#############################################
#6

# def action (a) :
#     if a % 3 ==0:
#         print(a%3)
#     if a % 7 ==0 :     
#          print(a%7)
#     else :
#         print("число не делиться на 3 и на 7 ")     

        
# a = int(input("Введите число"))

# action(a)


#################################################
# def P (a):
#     pr = 4 * a
#     print(pr)


# a = int(input("Введите знач"))

# P(a)


# def Sh (storon):
#     S = storon**2
#     print(S)

# c = int(input("Введите знач"))

# Sh(c)

###################################################

# # def action(a1 , a2 , a3 , a4 ,a5 ,a6 ):
# #     a1 = a1*3
# #     a2 = a2 *3
# #     a3 = a3 *3
# #     a4 = a4 *3
# #     a5 = a5 *3
# #     a6 = a6 *3
# #     print(a1,a2,a3,a4,a5,a6)


# # a = 1

# # b = 3

# # c = 5

# # d = 7

# # s = 1981

# # f = 773


# action(f,b,d,c,s,a)


a = [1,332,4343,566,11,44]

summ , i = 0 , 0 

while i < len (a):
    summ = summ + a[i]
    print(summ) 
    i = i + 1
    print(i)

# print()
