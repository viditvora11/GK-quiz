'''
creating a dictionaries, list and functions like def
and try and except.
'''
print("====================================")
print("Welcome to a genral knowlage quiz.")
print("====================================")
import datetime
a = datetime.datetime.now()
print("----You have joined this quiz at----\n","---",a,"---")
print("====================================")
'''
Using dictionary for writing the questions and correct
answers to the questions.
'''
gkquiz = {
'1.:a',
'2.:b',
'3.:c',
'4.:d',
'5.:a',
'6.:b',
'7.:c',
'8.:d',
'9.:a',
'10.:b',
}

#Using list for writing all the options for each question
optlist = [
'a. 1\n:b. 2\n:c. 3\n:d. 4'
'a. 1\n:b. 2\n:c. 3\n:d. 4'
'a. 1\n:b. 2\n:c. 3\n:d. 4'
'a. 1\n:b. 2\n:c. 3\n:d. 4'
'a. 1\n:b. 2\n:c. 3\n:d. 4'
'a. 1\n:b. 2\n:c. 3\n:d. 4'
'a. 1\n:b. 2\n:c. 3\n:d. 4'
'a. 1\n:b. 2\n:c. 3\n:d. 4'
'a. 1\n:b. 2\n:c. 3\n:d. 4'
'a. 1\n:b. 2\n:c. 3\n:d. 4'
]

index = 0
score = 0
optnumb = 0

#using def to welcome and using .isalpha to trap errors
def greet():
    while True:
        name = input("Please enter your name here : ")
        if name.isalpha():
            break
        print("Please enter your name in characters only.")
greet()


#using def to welcome and using .isnumeric to trap errors
def age():
    while True:
        age = input("Please enter your age : ")
        if age.isnumeric():
            break
        print("Please enter you age in numbers only.")
age()

status = input("Are you ready to take this genral knolage quiz?\npress y to continue or n to exit : ")

if status == "y" or status == "yes" or status == "YES" or status == "Y" or status == "YeS":
    print("Welcome to the quiz.")
    
rule = input("Do you want to know the instructions for the quiz?\npress y to learn the instructions and n to play without instructions : ")
if rule == "y" or status == "yes" or status == "YES" or status == "Y" or status == "YeS":
    print("print instructions")

#asking question
    for q in gkquiz.keys():
        print(q)#This will ask questions one by one in order.
        print(optlist[index])
        index = index+1
        print("********************************")

        user_ans = input("Enter you answer")
        answer = sportsquiz[q]

        if user_ans == answer:
            print("Nailed it lets keep going.")
            score = score+1
            print("you score is",score+0)
        else:
            print("Good try lets keep going. The right answer is",answer)
            print("=============================")

    print("Your score is",score,"out of 10 points")
    print("Quiz is over , welldone")

    exit()

elif status == "no" or status == "nO" or status == "n" or status == "NO" or status == "N":
    print("Please consider playing this quiz again.")

elif rule == "no" or status == "nO" or status == "n" or status == "NO" or status == "N":
    print("lets continue playing without the rules")
    

