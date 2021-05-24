from random import shuffle

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

rounds()



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

            del gkquiz[0]
            r-=1
            break
        else:
            print("Please enter your answer in a,b,c,d only")
