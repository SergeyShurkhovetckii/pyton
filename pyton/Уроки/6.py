
def action (b1 , a):
    for p in a:
        for b in p:
            if b == b1:
                print(p)


b = str(input("Введите слово "))


a = ['clean','memory','python']


action( b , a )


p = 'machine'

for b in p:
    print(b)



######################################


def action(d1 , a):
    for i in a :
        for d in i:
            if d == d1:
                print(i)        


b = input('Введите  словосочетание')

#1
if len(b) > 1 :
    print("Вы ввели больше одного символа")

    
else :
    a = ['red','whithe', 'blue', ' cat' , 'skainer']    
    action(b , a )
    
2

count = 0 


for i1 in b :
    count = count + 1 
if count > 1 :
    print("нужно 1 символ")
else:
    a = ['red','whithe', 'blue', ' cat' , 'skainer']   
    action(b , a )



########################################################
def action (a1 , b):
    for i in a1 :
        if i == b :
            print("Есть такая буква" + i )
        else:
            print("Нету такой буквы")
            

a = input('Введите слово')

b = input('Что нужно найти')


action (a , b )




