import math

TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining >0 :
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?  ")
    number_of_tickets = input("Hi {}, how many tickets do you want?  "
                              .format(name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("Sorry, only {} tickets remaining." +
                    "".format(tickets_remaining))
    except ValueError as err:
        print("Oops, ran into an issue. {} Try again.".format(err))
    else:
        total_price = TICKET_PRICE * number_of_tickets
        print("Your total price is ${}".format(total_price))  
        confirm_purchase = input("Do you want to continue and " + 
                                 "purchase tickets? Type Y or N  ")
        if confirm_purchase.lower() == "y":
            # TODO: Get credit card information and process purchase
            print("Sold! Thanks for shopping with us {}".format(name))
            tickets_remaining = tickets_remaining - number_of_tickets
        else:
            print("Thanks for shopping with us and have a nice day {}".format(name))       
print("The tickets are sold out!")
                         
