#Design a program that asks the user to enter a store’s sales for each day of the week. The amounts should be stored in a list. 
#Use a loop to calculate the total sales for the week and display the result


def weeklySalesCalculations():

    #storing days of the week
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #list to store the sales for each day
    sales = []

    #weekly Total Sales Amount
    weeklyTotalSales = 0 


    #prompting user to enter sales amount for each day of the week
    for day in days:
        salesAmount = int(input(f"Enter the sales amount for {day}: "))
        sales.append(salesAmount)


    #loop to calculate the weekly total sales
    for sale in sales:
        weeklyTotalSales+=sale
    print(f"The total weekly sales for the store is:  {weeklyTotalSales:,}") 




#calling function
weeklySalesCalculations()    

