#import
import time
#for score machanics
b = 1
c = 100
score = 0
#printing questions
print('What element has a symbol Sn?')
print("\na)Chlorine\nb)Sulfur\nc)Strontium\nd)Tin\n")

#checking answers
while True:
    user_answer = input("Please enter your answer here : ")
    if user_answer == 'a' or user_answer == 'b' or user_answer == 'c' or user_answer == 'd':
        if user_answer == 'd':
            print("===============================")
            print("nailed it keep it up, good work")
            print("===============================")
            score +=1 #increasing score
            print("================")
            print("Your score is",score)
            print("================")
        else:
            print("==============================================================")
            print("Sorry the option you have chosen is not right. The answer is d")#printing right answer
            print("==============================================================")
        break #ending the loop
    else:
        print("Please enter your answer in a,b,c,d only")

        
print("Your score is ",score,"out of 1") #Show the score and stats for the end of the quiz.
print("The precentage of the score is",score/b*c,"%")#Showing percentage
print("You have ended the quiz successfully,Welldone.")
print("\nThank you please join us to play the quiz again \nYou can email me at 19022@students.mrgs.school.nz \nif you want to challange me to make another quiz or change something in the quiz.")
time.sleep(7) #pausing the code for 7 seconds
exit()#asking if they want to leave the quiz
