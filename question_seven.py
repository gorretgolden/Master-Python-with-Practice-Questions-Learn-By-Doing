# Write a  Python program to convert temperatures to and from Celsius and Fahrenheit. 
# Formulae F = (9/5C+32)

def temperatureConvertions():

    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius ")

    option = int(input("Select your choice (1 or 2): "))

    if option == 1:
        celsius =  float(input("Enter temperature in Celsius Degrees: "))
        fahrenheit  = (9/5 * celsius) + 32
        print(f"{celsius}° C is equal to {fahrenheit}°F")

    elif option == 2:
        fahrenheit =  float(input("Enter temperature in Fahrenheit Degrees: "))
        celsius  = 5/9 * (fahrenheit -32 )
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid option!") 


temperatureConvertions()