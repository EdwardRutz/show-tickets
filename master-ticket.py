TICKET_PRICE = 10

tickets_remaining = 100

print("There are {} tickets remaining.".format(tickets_remaining))

#Get user's name and assign it to a variable
name = input("What is your name?  ")

#Prompt user by name and get number of tickets they want.
number_of_tickets = input("Hi {}, how many tickets do you want?  "
                          .format(name))
number_of_tickets = int(number_of_tickets)

#Calculate the price and assign it to a variable

total_price = TICKET_PRICE * number_of_tickets
# total_price = TICKET_PRICE * int(number_of_tickets)

print("Your total price is ${}".format(total_price))
# print("Your total price is $" + str(total_price))



