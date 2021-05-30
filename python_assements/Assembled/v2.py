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

index=0
score=0
optnum=0

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

#Asking the user if they are ready for the quiz

ready=input("Are you ready for the quiz?: press y to continue or x to exit:")

if ready=="y" or ready == "yes" :
    print("lets continue")
    print("---------------------------------------------")
    print("Please answer the questions with the the alphabets (a,b,c,d)")
    print("---------------------------------------------")

rule = input("Do you want to know the instructions for the quiz?\npress y to learn the instructions and n to play without instructions : ")

if rule == "y" or status == "yes" or status == "YES" or status == "Y" or status == "YeS":
    print("print instructions")
    
        #Questions for Sports Quiz.
    for q in sportsquiz.keys():
        print(q) #Printing one question at a time in order.
        print(optlist[index]) #Print first option.
        index=index+1
        print("            ")
        
        user_ans=input("Enter your answer:")
        answer = sportsquiz[q] # Finding answer to the question in the dictionary.

        if user_ans==answer:
            print("That is correct, Keep up the good work")
            print("---------------------")
            score=score+1
            print("Score",score+0)
        else:
            print("That is not correct. The answer is", answer)


            

            print("---------------------")
               

    print("Your score is",score,"out of 10 points")  #Presenting the scores to the users.
    print("Quiz Complete, WELL DONE :)")

    exit()

    
elif ready== "n" :  #If the user inputs x or no, when they are asked if they want to contiue the quiz or not.
    print("Consider playing later")
elif ready== "no":
    print ("please Consider playing the quiz with us")
