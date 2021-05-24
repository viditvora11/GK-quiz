index = 0
score = 0
optnum = 0

gkquiz = {
"1.What is the difference in the number of stars in australia's flag and new zealand's flag":'a',
}

optlist = ['a)1\nb)2\nc)3\nd)4']

for q in gkquiz.keys():
        print(q) 
        print(optlist[index]) 
        index=index+1
        print("            ")
        
user_answer = input("Please enter your answer here : ")
if user_answer == 'a' or user_answer == 'b' or user_answer == 'c' or user_answer == 'd':
    if user_answer == 'a':
        print("===============================")
        print("nailed it keep it up, good work")
        print("===============================")
        score +=1 
        print("================")
        print("Your score is",score)
        print("================")
    else:
        print("==============================================================")
        print("Sorry the option you have chosen is not right. The answer is a")
        print("==============================================================")
        
print("Your score is",score,"out of 1 points")  #Show the score and stats for the end of the quiz.
print("You have ended the quiz succesfully, WELLDONE.")
