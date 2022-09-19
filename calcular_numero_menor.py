

# num1 = input('Give me the first number:  ')
# num2 = input('Give me the second number:  ')
# num3 = input('Give me the third number:  ')

# if num1 < num2 and num1 < num3:
#     print(f'El numero {num1} es menor')
# elif num2 < num1 and num2 < num3:
#     print(f'El numero {num2} es menor')
# else:
#     print(f'El numero {num3} es menor')

# my_list1 = [n for n in range(101) if n % 2 == 0]
# print(my_list1)
def es_primo():

    for i in range(2, 101):
        for j in range(2, i):
            if(i % j == 0):
                print(i)
                continue
            print(i)

# def es_primo(num):
#     for n in range(2, num):
#         if num % n == 0:
#             print('No es primo')
#             return False
#         print('Es primo')
#         return True    

# es_primo(11)






