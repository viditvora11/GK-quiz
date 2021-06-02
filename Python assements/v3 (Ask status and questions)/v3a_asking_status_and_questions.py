#asking status
status = input("\nAre you ready for testing your general knowledge through our quiz? \n press y to continue or x to exit : ")
if status == "y" or status == "yes" :
    print("\nThank you for choosing our quiz for testing your general knowledge lets keep going")
elif status == 'x' or status == 'no':
    exit()

#Right answers to the question
Q1 = 'shape of you'
Q2 = 'Joe Biden'
Q3 = 'Vos savant'
Q4 = 'Walmart'
Q5 = 'Toyota'
score = 0

#question 1
print("\nQuestion: 1|score:{}".format(score))
ans=input("What is the most famous song in the world in 2020?\n\na.shape of you\nb.Despasito\nc.closer\n\nYour answer : ")
if ans == 'shape of you' or ans == 'Shape of you' or ans =='A' or ans == 'a': #Checking answers
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is :" ,Q1)
    if score <=0:#increasing score
        score = 0
        print("Your score is",score)

#question 2
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

#question 3
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

#question 4
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

#question 5
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
