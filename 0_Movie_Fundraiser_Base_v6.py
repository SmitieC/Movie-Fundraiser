"""Added ticket calc price and total calc"""


# Import Statements

# Functions go here
# Function check that ticket name is not blank
def calculate_ticket_price(age):
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if age in child_age:
        ticket_price = child_price
    elif age in standard_age:
        ticket_price = standard_price
    else:
        ticket_price = retired_price
    return ticket_price


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
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
profit = 0

while name != "Xxx" and ticket_count != MAX_TICKETS:
    if MAX_TICKETS - ticket_count > 1:
        print(f"\nThere are {MAX_TICKETS - ticket_count} tickets left")
    else:
        print(f"\n*****There are ONE ticket left*****")
    # Get details
    # Get name (cannot be blank)
    name = not_blank("What is your name: ")
    if name != "Xxx":
        break
    else:
        MINIMUM_AGE = 12
        MAX_AGE = 110
        age = number_checker(f"Please enter {name}'s age: ")
        if age < MINIMUM_AGE:
            print(f"\nSorry, you are too young to order a ticket")
        else:
            while not age <= MAX_AGE:
                age = number_checker(f"\nAt {age} {name} is very old."
                                     f"\nPlease re-enter {name}'s age: ")
            ticket_count += 1

            # Calculate ticket price
            ticket_price = calculate_ticket_price(age)
            print(f"For {name} the price is {ticket_price:,.2f}")
            profit += (ticket_price - TICKET_COST_PRICE)
# Calculate total sales and total profit

if ticket_count < MAX_TICKETS:
    if ticket_count > 1:
        print(f"\n {ticket_count} tickets have now been sold")
    else:
        print(f"1 ticket has been sold")
    if MAX_TICKETS - ticket_count > 1:
        print(f"\nThere are {MAX_TICKETS - ticket_count} tickets left")
    else:
        print(f"\n*****There is ONE ticket left*****")
else:
    print(f"\nYou have sold all of the available tickets")
    print("*" * 60)

print(f"\nThe total profit is {profit:,.2f}")
    # Loop to ask for snacks

    # Calculate Snack price

    # Ask for payment method (apply surcharge if credit card)

# Ouput data to text file
