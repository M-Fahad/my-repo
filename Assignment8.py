# Define functions for each operation

def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers, with zero-division check"""
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def calculator():
    """Main function to handle user input and perform calculations"""
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        # Take input from the user to select an operation
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the choice is valid
        if choice in ['1', '2', '3', '4']:
            # Take the input numbers from the user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the selected operation
            if choice == '1':
                print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
        else:
            print("Invalid Input!")

        # Ask if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

# Run the calculator
calculator()
