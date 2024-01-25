# pseudocode

# Create a function that will determine if the number is the same if reversed
def palindrome(number):
    number_str = str(number)

    reversed_str = number_str[::-1]
    return number_str == reversed_str

# User input a number
user_input = input("Please enter a number: ")

# Lock the input into interger only
user_number = int(user_input)

# if-else statement that will call the function / results