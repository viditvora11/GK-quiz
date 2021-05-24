#This is a simple quiz
Q1 = 'shape of you'
Q2 = 'Joe Biden'
Q3 = 'Vos savant'
Q4 = 'Walmart'
Q5 = 'Toyota'

#initial score
score = 0
#Ask for name
while True:
    name = input("Please enter your name : ")
    if name.isalpha():
        break
    print("Please enter your name in characters only")

#Ask for age
while True:
    age = input("\nPlease enter your age : ")
    if age.isnumeric():
        break
    print("Please enter your age in numbers only")


#Ask if they are ready to take the quiz
while True:
    status = input("\nAre you ready to take the quiz :{}?: \na. Yes \nb. No \n=>".format(name))
    if status.isalpha():
        break
    print("Please enter status in characters only")

#What if the user is not ready
if status == 'No' or status == 'no' or status == 'n' or status == 'N' : 
    print("See you soon.")
    
#what if the user is ready
if status == 'yes' or status == 'Yes' or status == 'y' or status == 'Y' or status == 'a' or status == 'A':
    print("Welcome to the quiz.")
 
#set of questions that are asked
#question 1

    print("\nQuestion: 1|score:{}".format(score))
    ans=input("What is the most famous song in the world in 2020?\n\na.shape of you\nb.Despasito\nc.closer\n\nYour answer : ")
    if ans == 'shape of you' or ans == 'Shape of you' or ans =='A' or ans == 'a':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is :" ,Q1)
        if score <=0:
            score = 0
            print("Your score is",score)

    print("\nQuestion: 2|score:{}".format(score))
    ans=input("What was the most famous person in the world in 2020?\n\na.Dwayne Jhonson\nb.Robert Downey jr\nc.Joe Biden \n\nYour answer : ")
    if ans =='C' or ans == 'c':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is :" ,Q2)
        if score <=0:
            score = 0
            print("Your score is",score)

    print("\nQuestion: 3|score:{}".format(score))
    ans=input("What is the smartest in the world in 2020?\n\na.Vos savant\nb.Kim ung yong \nc.Aryabhatta \n\nYour answer : ")
    if ans =='A' or ans == 'a':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is :" ,Q3)
        if score <=0:
            score = 0
            print("Your score is",score)

    print("\nQuestion: 4|score:{}".format(score))
    ans=input("Which company is the most famous company in the world for 2020?\n\na.Apple\nb.Walmart\nc.Amazaon\n\nYour answer : ")
    if ans =='b' or ans == 'B':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is :" ,Q4)
        if score <=0:
            score = 0
            print("Your score is",score)

    print("\nQuestion: 5|score:{}".format(score))
    ans=input("which company is the most famous car company in 2020?\n\na.BMW\nb.Ford\nc.Toyota\n\nYour answer : ")
    if ans =='C' or ans == 'c':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is :" ,Q5)
        if score <=0:
            score = 0
            print("Your score is",score)
