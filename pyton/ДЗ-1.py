#########################
#1
a = [9,4,3,7,8]

print(max(a))
print(min(a))
print(max(a)-min(a))


#######################
#2
a = [9,4,3,7,8]

print(sum(a)-max(a))

########################
#3
a = [9,4,3,7,8]
b = [12,21,75,96]

a.extend(b)
print(a)

print (max(a))
###########################
#4
a = [9,4,3,7,8]

print(len(a))

a.remove(9)
print(a)

a.append(50)

print(a)
######################
#Добавить данные в середину 
######################



##################################
#5

x = int(input())
y = int(input())

print(x+y)

print(x-y)

print(x/y)

print(x*y)

###################################
#6

name = 'Valentin'
surname = 'Flop'
age = 20 

print('My name is {name1}, My surname is {surname1}, its {age1}'.format(name1=name, surname1=surname, age1=age ))



