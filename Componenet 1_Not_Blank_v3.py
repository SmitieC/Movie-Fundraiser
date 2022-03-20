""" Not Blank Function"""


def not_blank(question):
    valid = ""
    while not valid.isalpha():
        valid = input(question)
        if valid == "" or valid.isalpha() != True:
            print("This cannot be blank...")
        else:
            return valid


# Main Routine
name = not_blank("What is your name: ")
