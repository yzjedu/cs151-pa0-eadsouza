

# Ask the user to enter a temperature in Celsius
celsius = input("Please enter the temperature in Celsius:")

#Change the input from a string to a number using "float"
celsius = float(celsius)

#Use the formula to actually convert Celsius to Farenheit
farenheit = (celsius * 9 / 5)  + 32

#Print the converted temperature
print("The temperature,",celsius,"degrees Celsius is equal to",farenheit, "degrees Fahrenheit.")

#Thank the user for using the converter.
print("Thank you for using the program!")