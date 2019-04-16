import pytest

def ticketsAvailable(total_tickets):
    tickets_remaining = total_tickets - 1
    return tickets_remaining






###### Tests ######

def test_canCallTicketsAvailable( ):
    ticketsAvailable(10)
    
def test_checkTicketsAvailableFormula( ):
    retVal = ticketsAvailable(100)
    assert retVal == "99"
    

