from random import shuffle
import datetime
import time
a = datetime.datetime.now()
b = 20
c = 100

#using dictionary for the question and the right answer to them
gkquiz =[
[
    "What is the difference in the number of stars in australia's flag and new zealand's flag",
    {'answer':'a','option':'a)1\nb)2\nc)3\nd)4\n'}
    ],
[
    "Who was the second person to step on the moon",
    {'answer':'b','option':'a)Pete conrad\nb)Buzz aldrin\nc)Neil armstrong\nd)Alan bean\n'}
     ],
[
    "What is the largest ocean",
    {'answer':'d','option':'a)Atlantic Ocean\nb)Indian ocean\nc)Arctic ocean\nd)Pacific ocean\n'}
     ],
[
    "Which country hosted the formula 1 race for the first time in 2011",
    {'answer':'c','option':'a)America\nb)Canada\nc)India\nd)Russia\n'}
     ],
[
    "Which animal is the most dangerous animal in the world",
    {'answer':'c','option':'a)Lion\nb)Tiger\nc)Nile crocodile\nd)Elephant\n'}
     ],
[
    "What comet passes near Earth every 76 years?",
    {'answer':'d','option':"a)Helley's Comet\nb)Comet Borrelly\nc)Tempel-tuttle Comet\nd)Halley's Comet\n"}
     ],
[
    "2, 3, 7, 11, and 19 are all examples of what type of number?",
    {'answer':'b','option':'a)Algebraic number\nb)Prime number\nc)Roman number\nd)Comosite number\n'}
     ],
[
    "In what country did espresso originate?",
    {'answer':'a','option':'a)Italy\nb)Africa\nc)America\nd)Russia\n'}
     ],
[
    "What element has the symbol Sn?",
    {'answer':'d','option':'a)Chlorine\nb)Sulfur\nc)Strontium\nd)Tin\n'}
     ],
[
    "What is the most common element in the earth's atmosphere?",
    {'answer':'b','option':'a)Oxygen\nb)Nitrogen\nc)Carbon dioxide\nd)Hydrogen\n'}
     ],
[
    "What are elephants afraid of?",
    {'answer':'a','option':'a)Mice\nb)Monkey\nc)Rabbit\nd)Water\n'}
     ],
[
    "What is the world's largest company by number of employees?",
    {'answer':'c','option':'a)Apple\nb)Tesla\nc)Walmart\nd)Amazon\n'}
     ],
[
    "How many cards are in a standard deck (not including jokers)?",
    {'answer':'b','option':'a)62\nb)52\nc)64\nd)54\n'}
     ],
[
    "Which email service is owned by Microsoft?",
    {'answer':'c','option':'a)Gmail\nb)Yahoo mail\nc)Hotmail\nd)icloud mail\n'}
     ],
[
    "Which animal can be seen on the Porsche logo?",
    {'answer':'d','option':'a)tapirs\nb)equidae\nc)donkey\nd)Horse\n'}
     ],
[
    "Which company owns Bugatti, Lamborghini. Audi, Porsche, and Ducati?",
    {'answer':'a','option':'a)Volkswagen\nb)Ford\nc)Jaguar\nd)Toyota\n'}
     ],
[
    "Which country invented tea?",
    {'answer':'a','option':'a)China\nb)America\nc)Africa\nd)India\n'}
     ],
[
    "Which watch company has a pointed crown as its logo?",
    {'answer':'d','option':'a)Omega\nb)Tissot\nc)Gshock\nd)Rolex\n'}
     ],
[
    "Who was the richest man in 2019?",
    {'answer':'c','option':'a)Mark zuckerberg\nb)Bill gates\nc)Jeff bezos\nd)Elon musk\n'}
     ],
[
    "Which app has the most downloads in 2019?",
    {'answer':'b','option':'a)Tiktok\nb)Whatsapp\nc)Instagram\nd)Facebook\n'}
     ],
]
shuffle(gkquiz)

index = 0
score = 0
optnum = 0

#using functions to ask name and .isalpha to trap errors.
def greet():
    while True:
        name = input("Please enter your name here : ")
        if name.replace(' ','').isalpha():
            break
        print("The data type you have used is invalid data type. (Please enter your name in alphabets only.)\n")
    
#Using functions to ask age and .isnumeric to trap errors as well.      
def age():
    while True:
        age = input("\nPlease enter your age : ")
        if age.replace(' ','').isnumeric():
            if 7< int(age)<125:
                break
            else:
                print('You need to be 7 to 125')
        else:
            print("The data type you have used is invalid data type.\n")
   

#Asking if they want to know the quiz rules.
def rule():
    rule = input("\nDo you want to read the rules or continue without the rules? \nPress y to learn the rules or any other key to continue without knowing the rules : ").lower()
    rule = rule.replace(' ','')
    if rule == "y" or rule == "yea" or rule == "yes":
        print("\nThe basic rules are as follows \n1. Enter the answer in a,b,c,d.\n2. Press enter if you don't know the answer.\n3. You are not allowed to use help of internet\n4. You can work with people but then the score will be your and the person you playing with.\nThe following options are just help for you.\nIf you press enter for a answer you will not get the point for it.\nRead the question and the options multiple times.")
    else:
        print("You may continue without the rules.")

#Asking thier status and if they want to keep going
def status():
    status = input("\nAre you ready for testing your general knowlage through our quiz? \nPress y to continue or any other key to exit :  ").lower()
    status = status.replace(' ','')
    if status == "y" or status == "yea" or status == "yes":
        print("\nThank you for choosing our quiz for testing your general knowlage lets keep going\n")
    else:
        print("\nThank you please play the quiz again you can email me at 19022@students.mrgs.school.nz\nif you want to challange me to make another quiz or change something in the quiz.")
        exit()

# I will be using dictionary, list and functions to create my quiz
print("               ===============================================")
print("               ******Welcome to a general knowledge quiz******")
print("               ===============================================")
print("               ---------You have joined this quiz at----------\n               ---------",a,"----------")
print("               ===============================================")
print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Disclaimer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("The quiz provided by us is for general knowledge and informative purpose only.\nAll information is provided in good faith and personal experience.\nWe make no representation or warranty of any kind regarding\nAccuracy,adequacy,validity,reliability or completeness of any information.\nYou can email me if you feel like your are offended my email is : \n19022@students.mrgs.school.nz")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Disclaimer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

greet()
age()
rule()
status()


while len(gkquiz)>0:
    data = gkquiz[0]
    q = data[0]
    data = data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)
    while True:
        user_answer = input("Please enter your answer here : ").lower()
        if user_answer == 'a' or user_answer == 'b' or user_answer == 'c' or user_answer == 'd':
            if user_answer == answer:
                print("===============================")
                print("nailed it keep it up, good work")
                print("===============================")
                score +=1 
                print("================")
                print("Your score is",score)
                print("================")
            else:
                print("==============================================================")
                print("Sorry the option you have chosen is not right. The answer is", answer)
                print("==============================================================")

            del gkquiz[0]
            break
        else:
            print("Please enter your answer in a,b,c,d only")


print("Your score is ",score,"out of 20") #Show the score and stats for the end of the quiz.
print("The precentage of the score is",score/b*c,"%")
print("You have ended the quiz successfully,Welldone.")
print("\nThank you please join us to play the quiz again \nYou can email me at 19022@students.mrgs.school.nz \nif you want to challange me to make another quiz or change something in the quiz.")
time.sleep(7)
exit()
