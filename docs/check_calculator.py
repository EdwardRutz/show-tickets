# Demo functions, math library and exceptions

import math

def split_check(total, number_of_people):
    if number_of_people <=1:
        raise ValueError("More than one person is required to split the check")
    cost_per_person = math.ceil(total / number_of_people)
    return cost_per_person     

try:
    total_due = float(input("What is the check total? "))
    number_of_people = int(input("How many people are splitting the check? "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as error:
    print("Oops, not a valid value. Try again...")
    print("{}".format(error))
else:
    print("Each person owes ${}".format(amount_due))
    
    
    
# Get check total and number of people
# output amount_due

# Todo This code causes a error in the test
# Set up the variables in the test








#Tests, see test_check-calculator

# def test_split_check_results():
#     assert split_check(40, 4) == 10

# TODO what is the best way to refactor the code?

# def split_check():
#     total_due = float(input("What is the check total? "))
#     number_of_people = int(input("How many people are splitting the check? "))
#     cost_per_person = math.ceil(total / number_of_people)
#     amount_due =  print("Each person owes ${}".format(cost_per_person))
#     return amount_due
    
# TODO get tip percentage
# TODO add tip
