"""This version checks if there's only one ticket left and if so,
it will print out a message"""
# Start of loop

# Initialize the loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nYou have {MAX_TICKETS - count} seats left.")
    else:
        print("\nYou have ONLY ONE seat left!")
    # Get details
    name = input("What is your name? ").title()
    count += 1

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still "
          f"{MAX_TICKETS-count} available")
else:
    print("\nYou have sold all the available tickets")
