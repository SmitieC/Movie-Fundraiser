""" Not Blank Function"""


def not_blank(question):
    valid = ""
    while not valid:
        valid = input(question)
        if valid == "":
            print("This can't be blank")
        else:
            return valid


# Main Routine
name = not_blank("What is your name: ")
