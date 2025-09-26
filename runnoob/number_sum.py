num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:    
    sum_result = float(num1) + float(num2)
    print(f"The sum of {num1} and {num2} is: {sum_result}")
except ValueError:
    print("Invalid input! Please enter numeric values.") 
# This code prompts the user to enter two numbers, calculates their sum, and handles invalid inputs gracefully. # It uses a try-except block to catch any ValueError that occurs if the input cannot be converted to a float.
# The code is a simple Python script that takes two numbers as input from the user, calculates their sum, and prints the result.                                
# # It also includes error handling to manage cases where the input is not a valid number.    


print('the result is: %.1f' %(float(input('Enter first number:'))+float(input('Enter second number:'))))