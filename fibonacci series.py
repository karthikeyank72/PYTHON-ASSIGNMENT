# This program prints the Fibonacci sequence
# up to a given number

def fibonacci(max):
  a, b = 0, 1
  while a < max:
    print(a, end=" ")
    a, b = b, a+b

# Get a number from user
max = int(input("Please enter a number: "))

# Print Fibonacci sequence
fibonacci(max)