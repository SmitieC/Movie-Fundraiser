def number_checker(question):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(question))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("\nPlease enter an integer (eg a whole number "
                  "with no decimal)")


# Main Routine
# Checks for a valid age
AGE_RANGE = range(12, 111)
age = number_checker("\nPlease enter age of ticker holder: ")
while age not in AGE_RANGE:
    age = number_checker("\nPlease enter integer between 12 and 110: ")

print(f"Age = {age}")
