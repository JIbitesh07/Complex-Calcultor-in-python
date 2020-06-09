calculation="start"

print("Hey User")
print("Welcome,please enter your inputs with operators")
print("When you are done with your calculations please enter 'end' or else you can continue")
print("")

while(calculation!="end"):
    calculation=input("Enter your numbers with operators ")  
    
    if calculation[len(calculation)-1].isdigit()==True  and calculation[1].isdigit()==True:
        print(calculation," = ",eval(calculation))

    elif calculation=="end":
        print("Ok bye. See you next time")

    else:
        print("Enter only digits and operators")
