import random
import datetime
# I will be using dictnary, list and functions to create my quiz
print("===============================================")
print("******Welcome to a general knowledge quiz******")
print("===============================================")
a=datetime.datetime.now()
print("---------You have joined this quiz at----------\n","---------",a,"---------")
print("===============================================")

#using dictionary for the question and the right answer to them
gkquiz = {
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
optlist = [
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

index = 0
score = 0
optnum = 0
#Using functions to ask name and .isalpha to trap errors.
def greet():
    while True:
        name = input("Please enter your name here : ")
        if name.isalpha():
            break
        print("The data type you have used is invalid data type. Please enter your name in alphabets only.")



#using functions to ask age and .isnumeric to trap errors as well.
def age():
    while True:
        age = input("\nPlease enter your age : ")
        if age.isnumeric():
            break
        print("The data type you have used is invalid data type. Please enter your age in numbers only.")



#Asking if they want to know the quiz rules.
def rule():
    rule = input("\nDo you want to read the rules or continue without the rules? \npress y to learn the rules or any other key to continue without knowing the rules : ")
    if rule == "y" or rule == "yes":
        print("\nThe basic rules are as follows \n 1. Enter the answer in a,b,c,d.\n 2. Press enter if you don't know the answer.\n(Know that you will not get the point for if you press enter)")
    elif rule == "x" :  #using elif to the previous if for asking if they want to know the rules to the quiz.
        print("You may continue without the rules.")
    elif rule == "no":
        print("You may continue without the rules.")
    

    
#Asking their status and if they want to keep going.
def status():
    status = input("\nAre you ready for testing your general knowledge through our quiz? \n press y to continue or x to exit : ")
    if status == "y" or status == "yes" :
        print("\nThank you for choosing our quiz for testing your general knowledge lets keep going")

greet()
age()
rule()
status()



# Asking questions for the quiz
for q in gkquiz.keys():
    print(q) #Printing one question every time from the dictnary.
    print(optlist[index]) #Printing the first options from the list.
    index = index+1
    print("            ")
        
    user_ans = input("please enter your answer here : ")
    answer = gkquiz[q] #finding the right answer to the question from the dictnary.

    if user_ans == answer:
        print("================================")
        print("nailed it keep it up, good work")
        print("================================")
        score = score+1
        print("================")
        print("your score is",score+0)
        print("================")  
    else:
        print("==============================================================")
        print("sorry the answer you have chosen is not right. The answer is", answer)
        print("==============================================================")



        print("Your score is",score,"out of 10 points")  #Show the score and stats for the end of the quiz.
        print("You have ended the quiz succesfully, WELLDONE.")

        time.sleep(4)
        exit()
   
