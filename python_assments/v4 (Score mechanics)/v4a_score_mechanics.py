#This is a simple quiz
Q1 = 'shape of you'
Q2 = 'Joe Biden'

score = 0

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
    
