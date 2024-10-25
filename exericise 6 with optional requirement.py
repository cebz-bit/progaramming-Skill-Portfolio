#Exercise 6: Brute Force Attack - 30 Marks

# Define what the correct password is
correct_password = "12345"
# Maximum number of attempts
max_attempts = 5
# attempt counter
attempts = 0

# Start of the password entry system
while attempts < max_attempts:
    # Prompt user for password input
    user_input = input("Please enter the password: ")
    
    # Check if the entered password is correct
    if user_input == correct_password:
        print("Access granted")
        break  # Exit the loop if the password is correct
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Incorrect password. You have {remaining_attempts} attempts left.")

# If the maximum attempts are reached
if attempts == max_attempts:
    print("Maximum attempts reached. Authorities have been alerted.")


