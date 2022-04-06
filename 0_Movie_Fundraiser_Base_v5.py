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


def number_checker(question):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(question))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("\nPlease enter an integer "
                  "(eg a whole number with no decimal)")


# Main Routine
# set up dictionary's and lists
# ask user if they have used the program before
# show instructions if they would like
# loop to get ticket details
# Initialize the loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nYou have {MAX_TICKETS - count} tickets left")
    else:
        print(f"\n*****You have ONE ticket left*****")
    # Get details
    name = input("What is your name? ").title()
    count += 1

    # Get name (cannot be blank)
    name = not_blank("What is your name: ")
    if name != "Xxx":
        break
    else:
        MINIMUM_AGE = 12
        MAX_AGE = 110
        age = number_checker("Please enter the age of the ticket holder: ")
        if age < MINIMUM_AGE:
            print(f"\nSorry, you are too young to order a ticket")
        else:
            while age <= MAX_AGE:
                age = number_checker(f"\nAt {age} {name} is very old."
                                     f"\nPlease re-enter {name}'s age: ")
            count += 1

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still "
          f"{MAX_TICKETS - count} tickets left")
else:
    print(f"\nYou have sold all of the available tickets")

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate Snack price

    # Ask for payment method (apply surcharge if credit card)

# Calculate total sales and total profit

# Ouput data to text file
