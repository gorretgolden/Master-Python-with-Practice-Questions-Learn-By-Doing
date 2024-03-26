Using a function and variables entered from the keyboard. Write a  program that allows a user to input a number.
If the input is an even number, returns the input divided by two plus 1. 
If the input is an odd number, returns the square of the input

 
def evenOrOddNumber():

    number = int(input("Enter a number: "))

    #even number
    if number %2 == 0:
        result = int((number/2) + 1)
        print("Number: Even "  +  "\nResult: " + str(result))
    else:
     #odd number
        result =  int(number ** 2)
        print("Number: Odd "  +  "\nResult: " + str(result))

           
evenOrOddNumber()









