
def calculatetyres():
    """
    Scenario
    A car servicing franchise requires a system that works out the price of a job on a car from the parts used and the labour required.
    The prices for parts are as follows:
    Item	Price
    Budget Tyre	29.99
    Premium Tyre	49.99
    Exhaust Pipe	69.99

    >>> calculatetypes('af')
    10.99

    Each job can have between 0-5 tyres. All the tyres must be the same type – either Budget or Premium. If the customer wants four or more tyres they get 20% discount on the tyres.
    Each job can then optionally have an exhaust pipe.
    If the customer buys and exhaust pipe AND any number of tyres (one or more) they get a £10 price reduction overall.
    Task: Create a program that		
    1)	Prompt the user for the number of tyres they require.
    2)	Accept the user input and store this in a suitable variable.
    3)	If they require one or more tyres, prompt and accept input for the type of tyres required: 
    ‘b’ for budget and ‘p’ for premium, storing the input in a suitable variable.
    4)	Prompt the user to see if they want an exhaust pipe, they enter ‘y’ they do. Accept input whether the user wants an exhaust pipe into a suitably typed variable.
    5)	Calculate the total price of the tyres based on their number and price. Use a selection statement to apply any discount required.
    6)	Calculate the total bill based on the tyre price and if applicable any price for an exhaust pipe.
    7)	Use a suitable selection statement to determine if there is an applicable discount based on purchasing both tyres and exhausts and apply this to the final total price.
    8)	Display the total final price
    9)	Prompt the user and wait for the user to press return to exit the programme.
    You do not have to worry about user data entry validation – i.e. the user will enter a number if prompted. 

    user input
    calculate total price of tyres based on number and price, including discount if activated
    discount is 20% off for four or more tyres
    additional discount if tyres (any number) and exhaust pipe bought together (£10 off)
    calc total bill based on above + exhaust if required
    display total final price and prompt the user to press return to exit
    """

    budgetprice = float(29.99)
    premiumprice = float(49.99)
    exhaustprice = float(69.99)
    howmanytyres = input('Enter the number of tyres you require: ')
    howmanytyres = int(howmanytyres)
    budget = input('Enter type of tyres required, "b" for budget or "p" for premium: ')
    exhaust = input('Enter y if you require an exhaust pipe: ')
    tyrecalc1 = float(0)
#    tyrecalc2 = float(0)
    finalbill = float(0)
    if howmanytyres > 0:
        if budget == 'b':
            tyrecalc1 = howmanytyres * budgetprice
            if howmanytyres >= 4:
                tyrecalc1 = tyrecalc1 * 0.8
        if budget == 'p':
            tyrecalc1 = howmanytyres * premiumprice
            if howmanytyres >= 4:
                tyrecalc1 = tyrecalc1 * 0.8
        if exhaust == 'y':
                tyrecalc1 = (tyrecalc1 + exhaustprice)
                finalbill = tyrecalc1 - 10
#                return finalbill
        if exhaust == 'n':
                finalbill = tyrecalc1
#                return finalbill
    if howmanytyres == 0:
        if exhaust == 'y':
            finalbill = exhaustprice
            return finalbill
        if exhaust == 'n':
            return 'if you no want tyre or exhaust why you waste my time!!'
    finalbill = round(finalbill, 2)
    return finalbill
if __name__ == '__main__':
        print(calculatetyres())
