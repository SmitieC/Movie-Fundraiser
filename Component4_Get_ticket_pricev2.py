"""Calculate ticket price by using the different ages"""


def calculate_ticket_price(age):
    CHILD_AGE = range(12, 16)
    STANDARD_AGE = range(16, 65)
    CHILD_PRICE = 7.5
    STANDARD_PRICE = 10.5
    RETIRED_PRICE = 6.5

    if age in CHILD_AGE:
        ticket_price = CHILD_PRICE
    elif age in STANDARD_AGE:
        ticket_price = STANDARD_PRICE
    else:
        ticket_price = RETIRED_PRICE
    return ticket_price


# main routine
name = input("Name: ")
age = int(input("Age: "))
print(f"The price for {name} is ${calculate_ticket_price(age):,.2f}.")
