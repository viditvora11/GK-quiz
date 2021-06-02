#Asking if they want to know the quiz rules.
def rule():#using def so that I can call it multiple times if needed
    rule = input("\nDo you want to read the rules or continue without the rules? \nPress y to learn the rules or any other key to continue without knowing the rules : ").lower()
    if rule == "y" or rule == "yea" or rule == "yes":
        print("\nThe basic rules are as follows \n1. Enter the answer in a,b,c,d.\n2. Press enter if you don't know the answer.\n3. You are not allowed to use help of internet\n4. You can work with people but then the score will be your and the person you playing with.\nThe following options are just help for you.\nIf you press enter for a answer you will not get the point for it.\nRead the question and the options multiple times.")
    else:
        print("You may continue without the rules.")

rule()

