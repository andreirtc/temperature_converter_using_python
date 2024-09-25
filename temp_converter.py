# 1. Ask user first if Celsius to Fahrenheit or Fahrenheit to Celsius
conversion_type = input("What conversion do you want to use?\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter your answer: ")
# 2. Ask the user to input temperature
temp_input = float(input("Enter the temperature: "))
# 3. Convert and print result
if conversion_type == '1':
    # Convert Celsius to Fahrenheit
    temp_output = (temp_input * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {temp_output}")
elif conversion_type == '2':
    # Convert Fahrenheit to Celsius
    temp_output = (temp_input - 32) * 5/9
    print(f"The temperature in Celsius is: {temp_output}")
else:
    print("Invalid conversion type. Please choose 1 or 2.")