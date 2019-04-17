# Notifications
def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 4)
    print(text)
    return result

# Output
yell("You are doing great")
yell("Don't forget to ask for help")
yell("Don't Repeat your logic. Keep Things DRY")
yell("uppercase letters")

## Notifications Tests

def test_yell_number_of_exclamations():
    """should give the correct number of exclamations"""
    assert yell("exclamations") == "EXCLAMATIONS!!!"
    

def test_yell_uppercase():
    assert yell("returns uppercase") == "RETURNS UPPERCASE!!!!"
    

# Basic Examples to test

def add_capital_case(text):
    result = text.capitalize()
    print(result)
    return result

add_capital_case("semaphore")

def test_add_capital_case():
    assert add_capital_case('semiphore') == 'Semiphore'


def f():
    return 3

def test_function():
    assert f() == 3, "value needs to be 3"

