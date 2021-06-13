#v1b_user_details
'''
this is my next change for asking user details. In the previous program the input
name allowed all inputs like integers, float and characters. This was the case in
all inputs. I will be adding the code to let it accept the specific datatypes for
the sutable inputs.
'''

#welcoming users
print("**************Welcome to the genral knowledge quiz*****************")
print("This quiz is devloped by vidit vora")

#asking name using .isalpha to trap errors 
while True:
    name = input("Please enter your name here : ")
    if name.isalpha():
        break
    print("Please enter name in alphabets only.")

#asking age using .isnumeric to trap errors 
while True:
    age = input("Please enter you age here : ")
    if age.isnumeric():
        break
    print("Please enter age in numbers only.")

#printing all users details 
print("Hello",name,"your age is",age)
