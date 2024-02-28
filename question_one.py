#QUESTION 1
# A Surveyor needs to prepare maps and adjust the coordinates of new location i.e. UTAMU
# New Campus parking yard. He usually uses this formula. ()
# Now he needs you design a python program to simplify his work in calculating the value
# of d.
# Ensure all values of Xi, X2, Y1, Y2 are entered from the keyboard. Values Xi =50, X2=20,
# Y1=150.5, Y2=98.8. 




#Importing required modules
import math


#Approach One
def valueOfD():
    
    X1 = int(input('Enter the value of X1:\t')) # int() Type Casting 
    X2 = int(input('Enter the value of X2:\t'))
    Y1 = float(input('Enter the value of Y1:\t')) #float()
    Y2 = float(input('Enter the value of Y2:\t')) 

    simplifiedExpression = (X1-X2) ** 2 + (Y1-Y2) ** 2
    d = math.sqrt(simplifiedExpression)
    #return d
    print("The value of d is: %.2f " %d + " ")
   
#calling the function  
valueOfD()


#Appproach Two
x_one = int(input('Enter the value of X1:\t')) # int() Type Casting 
x_two = int(input('Enter the value of X2:\t'))
y_one = float(input('Enter the value of Y1:\t')) #float()
y_two = float(input('Enter the value of Y2:\t')) 

def approachTwo(X1,X2,Y1,Y2):
    
    d = math.sqrt((X1-X2) ** 2 + (Y1-Y2) ** 2) #d expression
    print("The value of d is: %.2f " %d)

approachTwo(x_one,x_two,y_one,y_two)

#NB: Decide to use one approach