# Your University decided to give 8% bonus to some employees if his/her year of 
# service is more than 4 years. 5% bonus for employees with 3 years of service. Else no 
# bonus. Write a program to ask the employee for their salary and year of service and display 
# the net bonus amount. Make sure you run the program until you decide to quit.


def employeeBonusCalculations():

    run = 1

    while run == 1:

        salary =  int(input("Enter your salary amount: "))
        yearsOfService =  int(input("Enter your years of service: "))

        if yearsOfService > 4:

            netBonusAmount = int((8/100 * salary))
            
        elif yearsOfService == 3:

            netBonusAmount = int((5/100 * salary))
        else:

            netBonusAmount = 0

        finalPay = salary + netBonusAmount     

        print(f"Your net bonus amount is: {netBonusAmount:,} and your final pay is {finalPay:,}")    

        run = int(input("Press 1 to continue or any number to quit: "))

        if run !=1:
            break


employeeBonusCalculations()