# Write a Python function to sum all the numbers in a list. Hint (apply a loop) 
# Sample List: (8, 2, 3, 0, 7) 
# Expected Output : 20

def sumOfListItems():

    numbers = [8,2,3,0,7]
    sum = 0

    for number in numbers:
        sum += number
    print("The sum of items in the list is:  " + str(sum))  

    


#calling the function
sumOfListItems()    
