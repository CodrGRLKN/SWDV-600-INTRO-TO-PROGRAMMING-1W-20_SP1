inputCelsisusString =input("Enter the temperature in Celsius: ")
tempInC = float(inputCelsisusString)

tempInF = 9 / 5 * tempInC + 32

print("The temperature in fahrenheit is", tempInF )

inputFahrenheitString = input("Enter the temperature in Fahrenheit: ")
tempInF = float(inputFahrenheitString)

tempInC = tempInF - 32 * 5 / 9

print ("The temperature in Celsius is", tempInC )