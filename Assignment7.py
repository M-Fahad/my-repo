import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a number is even or odd
def even_or_odd(num):
    return "even" if num % 2 == 0 else "odd"

# Greet the user and get their name
name = input("Enter your name: ")

# Get the user's three favorite numbers
numbers = []
numbers.append(int(input("Enter your first favorite number: ")))
numbers.append(int(input("Enter your second favorite number: ")))
numbers.append(int(input("Enter your third favorite number: ")))

# Greet the user
print(f"\nHello, {name}! Let's explore your favorite numbers:")

# Check if numbers are even or odd and print the results
for num in numbers:
    status = even_or_odd(num)
    print(f"The number {num} is {status}.")

# Create and print tuples of each number and its square
for num in numbers:
    print(f"The number {num} and its square: ({num}, {num**2})")

# Calculate the sum of the numbers
total_sum = sum(numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

# Check if the sum is a prime number
if is_prime(total_sum):
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"The sum {total_sum} is not a prime number, but it's still great!")
