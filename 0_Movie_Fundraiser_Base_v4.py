"""Added Loop code to the base version of the Movie Fundraiser."""


# Import Statements

# Functions go here
# Function check that ticket name is not blank
def not_blank(question):
    valid = ""
    while not valid.isalpha():
        valid = input(question)
        if valid == "" or valid.isalpha() != True:  # Checks if input is blank
            print("This cannot be blank...")  # Error message
        else:
            return valid  # Returns valid input

def number_checker(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("\nPlease enter an integer "
                  "(eg a whole number with no decimal)")


# Main Routine

    # Main

    # set up dictionary's and lists

    # ask user if they have used the program before
    # show instructions if they would like

    # loop to get ticket details
# Initialize the loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != MAX_TICKETS:
    # Get details
    name = input("What is your name? ").title()
    count += 1

    # Get name (cannot be blank)
    name = not_blank("What is your name: ")

    # Get age (must be between 12 and 130)
MIN_AGE = 12
MAX_AGE = 110
# Get User Age
age = number_checker("\nPlease enter age of ticker holder: ")
if age < MIN_AGE:
    print(f"\nYou must be at least {MIN_AGE} years old to buy a ticket")
else:
    while age <= MAX_AGE:
        age = number_checker(f"\nPlease enter integer "
                             f"between {MIN_AGE} and {MAX_AGE}: ")

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate Snack price

    # Ask for payment method (apply surcharge if credit card)

# Calculate total sales and total profit

# Ouput data to text file
