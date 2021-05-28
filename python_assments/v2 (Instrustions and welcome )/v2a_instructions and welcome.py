#Asking if they want to know the quiz rules.
rule = input("\nDo you want to read the rules or continue without the rules? \npress y to learn the rules or x to continue without knowing the rules : ")
if rule == "y" or rule == "yes": 
    print("\nThe basic rules are as follows \n 1. Enter the answer in a,b,c,d.\n 2. Press enter if you don't know the answer.\n(Know that you will not get the point for if you press enter)")
elif rule == "x" :  #using elif to the previous if for asking if they want to know the rules to the quiz.
    print("You may continue without the rules.")
elif rule == "no":
    print("You may continue without the rules.")


