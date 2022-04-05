def integer_checker(question, low_num, high_num):
    error = f"Please enter an integer between {low_num} and {high_num}."
    valid = False
    while not valid:
        # asking user for a number and check to see if it is valid
        try:
            number_to_check = int(input(question))
            if low_num <= number_to_check <= high_num:
                return number_to_check
            else:
                print(error)
        except ValueError:
            print("\nPlease enter a integer (ie a whole number "
                  "with no decimal)")


# main routine
# checks for a valid age - must be between 12 and 11-
age = integer_checker("\nPlease enter age of ticker holder: ", 12, 110)
print(f"Age = {age}")
