#Component 1 asking name, age, yearlvl and v1
'''
There will be no question iincluded I will be adding the question only the final
version because This is only for the components.
'''
#Asking Name
while True:
    name = input("Please enter your name : ")
    if name.isalpha():
        break
    print("Please enter letter only.")

#Asking Age 
age = int(input("Please enter your age : "))

#Asking Year level
yearlvl = int(input("Please enter your year level : "))

#Asking Status
while True:
    status = str(input("Please enter y to start the quiz and n to stop the quiz."))
    if status.isalpha():
        break
    print("Please enter letter only")

print("Hello",name,"you are",age,"and your year level is",yearlvl,"Thank you for playing this game with us." )
