import datetime
import random

q1 = "hi"
q2 =
q3 =
q4 =
q5 =
q6 =
q7 =
q8 =
q9 =
q10 =

o1 =
o2 =
o3 =
o4 =
o5 =
o6 =
o7 =
o8 =
o9 =
o10 =

r1 =
r2 =
r3 =
r4 =
r5 =
r6 =
r7 =
r8 =
r9 =
r10 = 

#using dictionary for the question and the right answer to them
dict_1 = {
1:[q1,o1],
}
dict_2 = {
2:[q2,o2],
}
dict_3 = {
3:[q3,o3],
}
dict_4 = {
4:[q4,o4],
}
dict_5 = {
5:[q5,o5],
}
dict_6 = {
6:[q6,o6],
}
dict_7 = {
7:[q7,o7],
}
dict_8 = {
8:[q8,o8],
}
dict_9 = {
9:[q9,o9],
}
dict_10 = {
10:[q10,o10],
}

#Using functions to ask name and .isalpha to trap errors.
def greet():
    
    while True:
        name = input("Please enter your first name here : ")
        if name.isalpha():
            break
        print("The input you have used is not valid. Please enter your name in alphabets only.")



#using functions to ask age and .isnumeric to trap errors as well.
def age():
    while True:
        age = input("\nPlease enter your age : ")
        if age.isnumeric():
            break
        print("The input you have used is not valid. Please enter your age in numbers only.")


#Asking if they want to know the quiz rules.
def rule():
    rule = input("\nDo you want to read the rules or continue without the rules? \npress y to learn the rules or any other key to continue without knowing the rules : ")
    if rule == "y" or rule == "yes" or rule == "yea" or rule == "Y" or rule == "YES" or rule == "YEA" or rule == "Yea" or rule == "Yes":
        print("\nThe basic rules are as follows ")
        print("1. Enter the answer in a,b,c,d.\n2. Press enter if you don't know the answer.\n(Know that you will not get the point for if you press enter)")
    else:#using else rather than elif so any other key will let them discontinue
        print("\nYou may continue without the rules.")

#Asking their status and if they want to keep going.
def status():
    status = input("\nAre you ready for testing your general knowledge through our quiz? \npress y to continue or any other key to exit : ")
    if status == "y" or status == "yes" or status == "yea" or status == "Y" or status == "YES" or status == "YEA" or status == "Yea" or status == "Yes":
        print("\nThank you for choosing our quiz for testing your general knowledge lets keep going")   
    else: #using else rather than elif so any other key will let them discontinue 
        print("\nPlease consider playing the quiz with us again.")
        exit()

greet()
age()
rule()
status()

print(dict_1)
a1 = input("please enter your answer : ")
if a1 == r1:
    print("Correct answer")
else:
    print("incorrect the right answer is",r1)

print(dict_2)
a2 = input("please enter your answer : ")
if a2 == r2:
    print("Correct answer")
else:
    print("incorrect the right answer is",r2)
    
print(dict_3)
a3 = input("please enter your answer : ")
if a3 == r3:
    print("Correct answer")
else:
    print("incorrect the right answer is",r3)
    
print(dict_4)
a4 = input("please enter your answer : ")
if a4 == r4:
    print("Correct answer")
else:
    print("incorrect the right answer is",r4)
    
print(dict_5)
a5 = input("please enter your answer : ")
if a5 == r5:
    print("Correct answer")
else:
    print("incorrect the right answer is",r5)
    
print(dict_6)
a6 = input("please enter your answer : ")
if a6 == r6:
    print("Correct answer")
else:
    print("incorrect the right answer is",r6)
    
print(dict_7)
a7 = input("please enter your answer : ")
if a7 == r7:
    print("Correct answer")
else:
    print("incorrect the right answer is",r7)
    
print(dict_8)
a8 = input("please enter your answer : ")
if a8 == r8:
    print("Correct answer")
else:
    print("incorrect the right answer is",r8)
    
print(dict_9)
a9 = input("please enter your answer : ")
if a9 == r9:
    print("Correct answer")
else:
    print("incorrect the right answer is",r9)

print(dict_10)
a10 = input("please enter your answer : ")
if a10 == r10:
    print("Correct answer")
else:
    print("incorrect the right answer is",r10)
    
