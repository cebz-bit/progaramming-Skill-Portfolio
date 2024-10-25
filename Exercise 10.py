#Exercise 10
def check_even_odd(number):
    """Function to check if a number is even or odd."""
    #checking if the number is even
    if number % 2 == 0:
        #if it is not even, a message shows saying it is odd
        return f"{number} is an Even Number."
    else:
        # If it is not even, a message shows saying it is odd
        return f"{number} is an Odd Number."

def main():
    #for asking the user to enter a number
    user_input = input("Please enter a number: ")
    
    try:
        #turning the input into an integer
        number = int(user_input)
        #calling the function to check if the number is even or odd
        result = check_even_odd(number)
        #printing for the result
        print(result)
    except ValueError:
        #if the input is not a number,it tells the user it's invalid
        print("Invalid input! Please enter a valid integer.")

# This runs the main function if the script is executed directly
if __name__ == "__main__":
    #starting the program by calling the main function
    main()
