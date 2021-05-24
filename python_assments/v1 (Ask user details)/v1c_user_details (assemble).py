#v1c_user_details
'''
this is my next change for asking user details. In the previous program the input
name doesn't allow anything other than the one it should accept but if any other
input is used it will say error and not let the user get another chance. I will be
changing the code to make it allow only the specific inputs and give chances.
'''



#Asking Name
while True:
    name = input("Please enter your name here : ")
    if name.replace(' ','').isalpha():
        break
    print("The data type you have used is invalid data type. (Please enter your name in alphabets only.))\n")
            
       

#Asking Age
while True:
    age = input("\nPlease enter your age : ")
    if age.replace(' ','').isnumeric():
        if 7< int(age)<125:
            break
        else:
            print('You need to be 7 to 125')
    else:
        print("The data type you have used is invalid data type.\n")
   



