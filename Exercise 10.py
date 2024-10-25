#Exercise 10
def check_even_odd(number):
    """Function to check if a number is even or odd."""
    # I check if the number is even
    if number % 2 == 0:
        # If it is even, I return a message saying so
        return f"{number} is an Even Number."
    else:
        # If it is not even, I return a message saying it is odd
        return f"{number} is an Odd Number."

def main():
    # I ask the user to enter a number
    user_input = input("Please enter a number: ")
    
    # Check if the input is a digit
    if user_input.isdigit():
        # Convert the input to an integer
        number = int(user_input)
        # I call the function to check if the number is even or odd
        result = check_even_odd(number)
        # I print the result message
        print(result)
    else:
        # If the input is not a valid number, I tell the user it's invalid
        print("Invalid input! Please enter a valid integer.")

# This runs the main function if the script is executed directly
if __name__ == "__main__":
    # I start the program by calling the main function
    main()
