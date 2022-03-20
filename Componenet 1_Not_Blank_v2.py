""" Not Blank Function"""


def not_blank(question,error):
    valid = ""
    while not valid:
        valid = input(question)
        if valid == "":
            print(error)
        else:
            return valid


# Main Routine
name = not_blank("What is your name: ", "This cannot be blank...")
