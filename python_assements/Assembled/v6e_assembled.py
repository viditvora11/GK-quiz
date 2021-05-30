import random
import datetime
import time
a = datetime.datetime.now()
b = 20
c = 100

#using dictionary for the question and the right answer to them
gkquiz = {
"1.What is the difference in the number of stars in australia's flag and new zealand's flag":'a',
"2.Who was the second person to step on the moon":'b',
"3.What is the largest ocean":'d',
"4.Which country hosted the formula 1 race for the first time in 2011":'c',
"5.Which animal is the most dangerous animal in the world":'c',
"6.What comet passes near Earth every 76 years?":'d',
"7.2, 3, 7, 11, and 19 are all examples of what type of number?":'b',
"8.In what country did espresso originate?":'a',
"9.What element has the symbol Sn?":'d',
"10.What is the most common element in the earth's atmosphere?":'b',
"11.What are elephants afraid of?":'a',
"12.What is the world's largest company by number of employees?":'c',
"13.How many cards are in a standard deck (not including jokers)?":'b',
"14.Which email service is owned by Microsoft?":'c',
"15.Which animal can be seen on the Porsche logo?":'d',
"16.Which company owns Bugatti, Lamborghini. Audi, Porsche, and Ducati?":'a',
"17.Which country invented tea?":'a',
"18.Which watch company has a pointed crown as its logo?":'d',
"19.Who was the richest man in 2019?":'c',
"20.Which app has the most downloads in 2019?":'b',
}

#using lists for the options to the relavant questions
optlist = [
'a)1\nb)2\nc)3\nd)4',
'a)Pete conrad\nb)Buzz aldrin\nc)Neil armstrong\nd)Alan bean',
'a)Atlantic Ocean\nb)Indian ocean\nc)Arctic ocean\nd)Pacific ocean',
'a)America\nb)Canada\nc)India\nd)Russia',
'a)Lion\nb)Tiger\nc)Nile crocodile\nd)Elephant',
"a)Helley's Comet\nb)Comet Borrelly\nc)Tempel-tuttle Comet\nd)Halley's Comet",
'a)Algebraic number\nb)Prime number\nc)Roman number\nd)Comosite number',
'a)Italy\nb)Africa\nc)America\nd)Russia',
'a)Chlorine\nb)Sulfur\nc)Strontium\nd)Tin',
'a)Oxygen\nb)Nitrogen\nc)Carbon dioxide\nd)Hydrogen',
'a)Mice\nb)Monkey\nc)Rabbit\nd)Water',
'a)Apple\nb)Tesla\nc)Walmart\nd)Amazon',
'a)62\nb)52\nc)64\nd)54',
'a)Gmail\nb)Yahoo mail\nc)Hotmail\nd)icloud mail',
'a)tapirs\nb)equidae\nc)donkey\nd)Horse',
'a)Volkswagen\nb)Ford\nc)Jaguar\nd)Toyota',
'a)China\nb)America\nc)Africa\nd)India',
'a)Omega\nb)Tissot\nc)Gshock\nd)Rolex',
'a)Mark zuckerberg\nb)Bill gates\nc)Jeff bezos\nd)Elon musk',
'a)Tiktok\nb)Whatsapp\nc)Instagram\nd)Facebook',
]

index = 0
score = 0
optnum = 0

#using functions to ask name and .isalpha to trap errors.
def greet():
    while True:
        name = input("Please enter your name here : ")
        if name.isalpha():
            break
        print("The data type you have used is invalid data type. (Please enter your name in alphabets only.)(Please don't use spaces if you have used spaces)\n")
            
#Using functions to ask age and .isnumeric to trap errors as well.      
def age():
    while True:
        age = input("\nPlease enter your age : ")
        if age.isnumeric():
            break
        print("The data type you have used is invalid data type. (Please enter your age in numbers only and please do not use spaces)\n")
   

#Asking if they want to know the quiz rules.
def rule():
    rule = input("\nDo you want to read the rules or continue without the rules? \nPress y to learn the rules or any other key to continue without knowing the rules : ").lower()
    if rule == "y" or rule == "yea" or rule == "yes":
        print("\nThe basic rules are as follows \n1. Enter the answer in a,b,c,d.\n2. Press enter if you don't know the answer.\n3. You are not allowed to use help of internet\n4. You can work with people but then the score will be your and the person you playing with.\nThe following options are just help for you.\nIf you press enter for a answer you will not get the point for it.\nRead the question and the options multiple times.")
    else:
        print("You may continue without the rules.")

#Asking thier status and if they want to keep going
def status():
    status = input("\nAre you ready for testing your general knowlage through our quiz? \nPress y to continue or any other key to exit :  ").lower()
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
print("The quiz provided by us is for general knowledge and informative purpose only.\nAll information is provided in good faith and personal experience.\nWe make no representation or warranty of any kind regarding\nAccuracy,adequacy,validity,reliability or completeness of any information.")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Disclaimer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

greet()
age()
rule()
status()

#Asking questions for the quiz
for q in gkquiz.keys():
    print(q) #Printing one question every time from the dictnary.
    print(optlist[index]) #Printing the first options from the list.
    index = index+1
    print(" ")

    user_ans = input("Please enter your answer here : ").lower()
    answer = gkquiz[q] #finding the right answer to the question from the question from the dictnary.

    if user_ans == answer:
        print("===============================")
        print("nailed it keep it up, good work")
        print("===============================")
        score = score+1
        print("================")
        print("Your score is",score+0)
        print("================")
    else:
        print("==============================================================")
        print("Sorry the option you have chosen is not right. The answer is", answer)
        print("==============================================================")

print("Your score is ",score,"out of 20") #Show the score and stats for the end of the quiz.
print("The precentage of the score is",score/b*c,"%")
print("You have ended the quiz successfully,Welldone.")
print("\nThank you please join us to play the quiz again \nYou can email me at 19022@students.mrgs.school.nz \nif you want to challange me to make another quiz or change something in the quiz.")
time.sleep(7)
exit()
