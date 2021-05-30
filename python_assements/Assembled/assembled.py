from random import shuffle
import datetime
import time
a = datetime.datetime.now()

#using functions to ask name and .isalpha to trap errors.
def greet():
    global name
    while True:
        name = input("Please enter your name here : ")
        if name.replace(' ','').isalpha():
            break
        print("The data type you have used is invalid data type. (Please enter your name in alphabets only.)\n")
   

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
        print("\nThank you for choosing our quiz for testing your general knowlage lets keep goings")
    else:
        print("\nThank you please play the quiz again you can email me at 19022@students.mrgs.school.nz\nif you want to challange me to make another quiz or change something in the quiz.")
        exit()

def rounds():
    global r , total
    while True:
        try:
            r = int(input("\nPlease enter how many rounds do you want to play there are a total of 20 round at max. : "))
            if 0<r<=20: 
                break
            else:
                print("Please enter the rounds in 1-20 only")
        except:
            print('Please enter rounds in numbers only (The max is 20)')
            

    
        
    total=r

    
#using dictionary for the question and the right answer to them
gkquiz =[
[
    "\nWhat is the difference in the number of stars in australia's flag and new zealand's flag",
    {'answer':'a','option':'a)1\nb)2\nc)3\nd)4\n'}
    ],
[
    "\nWho was the second person to step on the moon",
    {'answer':'b','option':'a)Pete conrad\nb)Buzz aldrin\nc)Neil armstrong\nd)Alan bean\n'}
     ],
[
    "\nWhat is the largest ocean",
    {'answer':'d','option':'a)Atlantic Ocean\nb)Indian ocean\nc)Arctic ocean\nd)Pacific ocean\n'}
     ],
[
    "\nWhich country hosted the formula 1 race for the first time in 2011",
    {'answer':'c','option':'a)America\nb)Canada\nc)India\nd)Russia\n'}
     ],
[
    "\nWhich animal is the most dangerous animal in the world",
    {'answer':'c','option':'a)Lion\nb)Tiger\nc)Nile crocodile\nd)Elephant\n'}
     ],
[
    "\nWhat comet passes near Earth every 76 years?",
    {'answer':'d','option':"a)Helley's Comet\nb)Comet Borrelly\nc)Tempel-tuttle Comet\nd)Halley's Comet\n"}
     ],
[
    "\n2, 3, 7, 11, and 19 are all examples of what type of number?",
    {'answer':'b','option':'a)Algebraic number\nb)Prime number\nc)Roman number\nd)Comosite number\n'}
     ],
[
    "\nIn what country did espresso originate?",
    {'answer':'a','option':'a)Italy\nb)Africa\nc)America\nd)Russia\n'}
     ],
[
    "\nWhat element has the symbol Sn?",
    {'answer':'d','option':'a)Chlorine\nb)Sulfur\nc)Strontium\nd)Tin\n'}
     ],
[
    "\nWhat is the most common element in the earth's atmosphere?",
    {'answer':'b','option':'a)Oxygen\nb)Nitrogen\nc)Carbon dioxide\nd)Hydrogen\n'}
     ],
[
    "\nWhat are elephants afraid of?",
    {'answer':'a','option':'a)Mice\nb)Monkey\nc)Rabbit\nd)Water\n'}
     ],
[
    "\nWhat is the world's largest company by number of employees?",
    {'answer':'c','option':'a)Apple\nb)Tesla\nc)Walmart\nd)Amazon\n'}
     ],
[
    "\nHow many cards are in a standard deck (not including jokers)?",
    {'answer':'b','option':'a)62\nb)52\nc)64\nd)54\n'}
     ],
[
    "\nWhich email service is owned by Microsoft?",
    {'answer':'c','option':'a)Gmail\nb)Yahoo mail\nc)Hotmail\nd)icloud mail\n'}
     ],
[
    "\nWhich animal can be seen on the Porsche logo?",
    {'answer':'d','option':'a)tapirs\nb)equidae\nc)donkey\nd)Horse\n'}
     ],
[
    "\nWhich company owns Bugatti, Lamborghini. Audi, Porsche, and Ducati?",
    {'answer':'a','option':'a)Volkswagen\nb)Ford\nc)Jaguar\nd)Toyota\n'}
     ],
[
    "\nWhich country invented tea?",
    {'answer':'a','option':'a)China\nb)America\nc)Africa\nd)India\n'}
     ],
[
    "\nWhich watch company has a pointed crown as its logo?",
    {'answer':'d','option':'a)Omega\nb)Tissot\nc)Gshock\nd)Rolex\n'}
     ],
[
    "\nWho was the richest man in 2019?",
    {'answer':'c','option':'a)Mark zuckerberg\nb)Bill gates\nc)Jeff bezos\nd)Elon musk\n'}
     ],
[
    "\nWhich app has the most downloads in 2019?",
    {'answer':'b','option':'a)Tiktok\nb)Whatsapp\nc)Instagram\nd)Facebook\n'}
     ],
]
shuffle(gkquiz)

index = 0
score = 0
optnum = 0

   
        

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
rounds()
rule()
status()




while r>0:
    data = gkquiz[0]
    q = data[0]
    data = data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)
    while True:
        user_answer = input("Please enter your answer here : ").lower().replace(' ','')
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
                print("Sorry the option you have chosen is not right. The answer is ",answer)
                print("==============================================================")
                print("================")
                print("Your score is",score)
                print("================")
                

            del gkquiz[0]
            r-=1
            break
        else:
            print("Please enter the alphabet for the chosen option") 
            


print(name,"Your score is ",score,"out of",total) #Show the score and stats for the end of the quiz.
print("The precentage of the score is",(round(score/total*100,2)),"%")
print("You have ended the quiz successfully, Welldone.")
print("\nThank you please join us to play the quiz again \nYou can email me at 19022@students.mrgs.school.nz \nif you want to challange me to make another quiz or change something in the quiz.")
time.sleep(7)
exit()
