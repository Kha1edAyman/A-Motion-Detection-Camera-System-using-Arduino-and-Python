# name = "Khaled"
# age = 21
# has_android_phone = "No"
# print(name, age, has_android_phone)

# person = dict(
#     dict_name = name, 
#     dict_age = age,
#     dict_has_android_phone = has_android_phone ,
# )
# print(f"hello {person["dict_name"]} your age is : {person["dict_age"]} and you don't has android phone" )


# My_list = ['Red' , 0 , True]

# print(My_list)
# print('My favorite color is', My_list[0])
# print(f'I have {My_list[1]} pets')

# if (My_list[2]):
#     print('I have programming experience.')
# else :
#     print("I Don't have programming experience.")

# My_list.append(1)
# del(My_list[0])

# print(My_list)


# problem 1

# for i in range(10,21):
#     is_prime =True 
    
#     for num in range (2, int (i**0.5) + 1):
#         if (i % num == 0) :
#             is_prime =False
#             break 
        
#     if  (is_prime) :
#         print(f"{i} is prime number")
        
        
        
# # problem 2

# fib_list = []
# a, b = 0, 1

# for I in range(10 ,21):
#     fib_list.append(a)
#     a, b = b, a + b

# print(fib_list)


# # problem3 

# balance = 1000

# while balance > 0:
#     amount = float(input("Enter amount to withdraw: "))

#     if amount <= balance:
#         balance -= amount
#         print(f"Remaining balance: {balance}")
#         if balance == 0:
#             print("Balance is zero. Exiting.")
#             break
#     else:
#         print("Insufficient balance.")


# problem 4

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = []


for item in list1:
    if item in list2:
        common_elements.append(item)

print(common_elements)
