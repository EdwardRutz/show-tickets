# Python Basics


4/19/19, Updated notes with code anywhere

------------------------------------------------
## Review

- What are the data types in Python?
- What is the order of math operations?
- What is the customary indent size in Python?
------------------------------------------------

## Skills

- Input and Output
- Conditional Branching
- math module
- Exception handling
- Looping
- Functions


## Types and Branching

- Numeric, Boolean, String 
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Text Sequence Type: str
Binary Sequence Types: bytes, bytearray, memoryview
Set Types: set, frozenset
Mapping Types: — dict
Other Built-in Types:
  - Modules, Classes and Class Instances, Functions, Methods, Code Objects, Type Objects, 
  - the Null Object (None), the Ellipsis Object, the NotImplemented Object, 
  - Boolean Values (True and False), Internal Objects.
  
- https://docs.python.org/3/library/stdtypes.html


### Numeric

- In the Python REPL, the underscore (_) temporarily stores the result of the previous calculation
- round(_)
- Order of opporations: PEMDAS, "Please Excuse My Dear Aunt Sally"
  - Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction
- Change a string to an integer, `int("11")`
- Change a string to a float, `float("11")`
- Divide and get an integer instead of a float (7.6), `23 // 3`
- Divide and get a remainder with a modulus, `23 % 3`, results in a remainder of 2



### If, Else, Elif

- One equal sign is used for assignment
- Two equal signs are used for comparison
- White space is important in python, it determines code structure
- Python uses 4 spaces for indents
- A block of code has the same indents
- End a block of code by returning to the starting indent

```python

first_name = input("What is your first name?  ")
print("Hello,", first_name) 
if first_name == "bob":
    print(first_name, "is learning Python")
elif first_name == "Susan"
	print("Susan is really enjoying Python.")
else:
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))	#New indent ends previous code block

```

```
favorite_color = input("What is your favorite color?  ")
if favorite_color == "blue":
	print("You must love the sky!")

```


## Functions and Looping

- Use Agile, create user stories, add stories to a Kanban board
- Copy Pasta, copying and pasting other people's code is not a good habit to get into
- Floor division or integer division uses two forward slashes (//) returns the floor integer.
  - Does use float-point to round down.
  - ` 5 // 2   # 2 and not 2.5 (or 3)
- Methods are owned functions, the String data type owns its method .upper()

- Import the Math Module and round up to next closest integer, ` math.ceil(21.24)`

- There is no need to create a variable just to return it.
- Refactor unused variables...
```python
cost_per_person = math.ceil(total / number_of_people)
return cost_per_person 

# Refactor, cost_per_person is never used, only returned so not needed
return math.ceil(total / number_of_people)
```
- The refactored version doesn't seem as clear and explicit as the original
- The variable, cost_per_person, clearly identifies what the expression does.

## Exception Handling

### Raise an Exception

```python
def split_check(total, number_of_people):
    if number_of_people <=1:
        raise ValueError("More than one person is required to split the check")
    cost_per_person = math.ceil(total / number_of_people)
    return cost_per_person  
```

### Try-Except-Else Block

- A common problem that occurs when programs receive input from a user is a coercion error. 
- The user provides data that is unable to be coerced.
- Put any code that might be problematic in a "try" block
- Add a try statement, `try: `

```python
try:
    total_due = float(input("What is the check total? "))
    number_of_people = int(input("How many people are splitting the check? "))
except ValueError:
    print("Oops, not a valid value. Try again...")
else:
    amount_due = split_check(total_due, number_of_people)
    print("Each person owes ${}".format(amount_due))
```

### Assign and Exception to a Variable

- Assign an exception to a variable with ` except ValueError as err `
```
def suggest(product_idea):
    if len(product_idea) < 3:
    	raise ValueError("Too short. Type more \
                         characters...")    
    return product_idea + "inator"
```

### While Loops

- Condition based looping. While this condition is true run this code.

```
# secret-code-checker.pytest

import sys

# while loop demo

MASTER_SECRET_CODE = opensesame
secret_code = input("Enter secret code?")
attempt_count = 1
while secret_code != 'MASTER_SECRET_CODE':
    if attempt_count >3:
        sys.exit("Too many invalid password attempts.")
    secret_code = input("Invalid secret code, try again...")
    attempt_count += 1
print("Welcome to secret town")
```

- Exit program with  an error, import `sys` and use `sys.exit`
	- ie, `sys.exit("Too many invalid password attempts.")`


# For Loops

- Interating through a set of values

```
banner = "Happy Birthday!"
for letter in banner
	print(letter.upper())
	
```


```
for letter in "You got this!":
    if letter in "oh":
        print(letter)	# ooh

```







## Creating an App

```python

# App to sell tickets.

import math

TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

# Create the calculate_price function
# returns number_of_tickets * price

def calculate_price(number_of_tickets):
    total_price = (TICKET_PRICE * number_of_tickets) + SERVICE_CHARGE
    return total_price

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?  ")
    number_of_tickets = input("Hi {}, how many tickets do you want?  "
                              .format(name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("Sorry, only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oops, ran into an issue. {} Try again.".format(err))
    else:
        amount_due = calculate_price(number_of_tickets)
        print("Your total price is ${}".format(amount_due))  
        confirm_purchase = input("Do you want to continue and " + 
                                 "purchase tickets? Type Y or N  ")
        if confirm_purchase.lower() == "y":
            # TODO: Get credit card information and process purchase
            print("Sold! Thanks for shopping with us {}".format(name))
            tickets_remaining = tickets_remaining - number_of_tickets
        else:
            print("Thanks for shopping with us and have a nice day {}".format(name))       
print("The tickets are sold out!")
 
```


------------------------------------------------
## Python Style Guide

- Use all caps for constant variables


## Pytest

- Importing into pytest, `from check_calculator import split_check`

## Projects

- show-tickets, A command-line app, ticket store


## Sources

- [Treehouse: Python Basics](https://teamtreehouse.com/library/python-basics-3)
- [PythonAnywhere.com](https://help.pythonanywhere.com)
- [Python Standard Library](https://docs.python.org/3/library/)
- [Python Math Module](https://docs.python.org/3/library/math.html)


