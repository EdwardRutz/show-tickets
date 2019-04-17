# Python Basics

## Types and Branching

- Numeric, String, Boolean

### Numeric

- In the REPL, the underscore (_) temporarily stores the result of the previous calculation
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

## Exceptions

### Raise an Exception

```python
def split_check(total, number_of_people):
    if number_of_people <=1:
        raise ValueError("More than one person is required to split the check")
    cost_per_person = math.ceil(total / number_of_people)
    return cost_per_person  
```

### Try-Except-Else Block

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


## Creating an App




------------------------------------------------

## Pytest

- Importing into pytest, `from check_calculator import split_check`

## Projects

- show-tickets, A command-line app, ticket store


## Sources

- [Treehouse: Python Basics](https://teamtreehouse.com/library/python-basics-3)
- [PythonAnywhere.com](https://help.pythonanywhere.com)
- [Python Standard Library](https://docs.python.org/3/library/)
- [Python Math Module](https://docs.python.org/3/library/math.html)


