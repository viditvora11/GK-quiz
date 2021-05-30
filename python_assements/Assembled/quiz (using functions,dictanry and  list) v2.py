# I will be using dictnary, list and functions to create my quiz
print("==============================================")
print("******Welcome to a genral knowalge quiz******")
print("==============================================")
import datetime
a=datetime.datetime.now()
print("---------You have joined this quiz at---------\n","--------",a,"-------")
print("==============================================")

#using dictionary for the question and the right answer to them
sportsquiz={
'1.Q1':'a',
'2.Q2':'b',
'3.Q3':'d',
'4.Q4':'c',
'5.Q5':'a',
'6.Q6':'d',
'7.Q7':'a',
'8.Q8':'d',
'9.Q9':'c',
'10.Q10':'c',
}

#using lists for the options to the relavant questions
optlist=[
'a)1\nb)2\nc)3\nd)4',
'a)1\nb)2\nc)3\nd)4',
'a)1\nb)2\nc)3\nd)4',
'a)1\nb)2\nc)3\nd)4',
'a)1\nb)2\nc)3\nd)4',
'a)1\nb)2\nc)3\nd)4',
'a)1\nb)2\nc)3\nd)4',
'a)1\nb)2\nc)3\nd)4',
'a)1\nb)2\nc)3\nd)4',
'a)1\nb)2\nc)3\nd)4',
]

index=0
score=0
optnum=0

#Using functions to welcome the people and using .isalpha to trap errors.

def greet():
    
    while True:
        name = input("Please enter your name here : ")
        if name.isalpha():
            break
        print("Please enter characters A-Z only")
greet()
print("Hello",greet,"welcome to our quiz")
#using .

while True:
    age=input("Please enter your age : ")
    if age.isnumeric():
        break
    print("The data type you have used is invalid data type. Please enter your age in numbers only.")

#Asking the user if they are ready for the quiz

status = input("Are you ready for testing your genral knowlage through our quiz? :\n press y to continue or x to exit : ")

if status == "y" or status == "yes" :
    print("Thank you for choosing our quiz for testing your genral knowlage lets keep going")
    print("---------------------------------------------")
    print("Please answer the questions with the the alphabets the folling alphabets only \n(a,b,c,d)")
    print("---------------------------------------------")
    
        #Questions for Sports Quiz.
    for q in sportsquiz.keys():
        print(q) #Printing one question at a time in order.
        print(optlist[index]) #Print first option.
        index=index+1
        print("            ")
        
        user_ans=input("please enter your answer here : ")
        answer = sportsquiz[q] # Finding answer to the question in the dictionary.

        if user_ans==answer:
            print("nailed it keep it up, good work")
            print("================================")
            score=score+1
            print("Score",score+0)
        else:
            print("sorry the answer you have chosen is not right. The answer is", answer)
            print("================================")
               

    print("Your score is",score,"out of 10 points")  #Presenting the scores to the users.
    print("You have ended the quiz succesfully, WELLDONE.")

    exit()

    
elif status == "x" :  #If the user inputs x or no, when they are asked if they want to contiue the quiz or not.
    print("please consider playing the quiz with us again.")
elif status == "no":
    print ("please consider playing the quiz with us again.")
