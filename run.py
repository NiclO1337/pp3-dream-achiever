# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def welcome():
    """
    Start application on a welcome screen with a message
    """
    print('\nWelcome message\n')
    input('Press ENTER to continue\n')


def dream():
    """
    Screen where user think about their dreams
    """
    print('Dream\n')
    input('Press ENTER to continue\n')


def goal(user):
    """
    Function to ask user to input a specific financial goal
    """
    print('Goal')

    while True:

        goal = input('Goal:\n')
        if validate_text(goal):
            user.update({"Goal": goal})
            return user


def get_data(user, data):
    """
    Ask user to input data
    """
    get_text(data)

    while True:

        data_input = input(f'{data}:\n')
        if validate_numbers(data_input):
            user.update({data: int(data_input)})
            return user


def get_text(data):
    """
    Function to print different messages
    depending on the category of data input
    """
    if data == "Cost of goal":
        print("\n\nEstimate the cost of your specified goal.\n")
        print("You do not have to specify which currency your cost is in,")
        print("but it is important to always stick to the same currency")
        print("throughout the calculator.")
        print("For example, if you live in Norway but have a salery in GBP")
        print("and like to order german sausages online and pay in EUR.")
        print("Convert all to whichever currency is easiest or you.\n")

    elif data == "Income":
        print("\n\nIncome\n")
        print("")
        print("")
        print("")
        print("")
        print("")

    elif data == "Extra income":
        print("\n\nExtra income\n")
        print("")
        print("")
        print("")
        print("")
        print("")

    elif data == "Housing":
        print("\n\nHousing costs\n")
        print("This would include mortgage payments, property taxes, strata")
        print("fees, rent, homeowner insurance, and hydro or electricity.\n")

    elif data == "Utilities":
        print("\n\nUtilities\n")
        print("Examples of utility costs are cell phone, gas, and internet")
        print("bills. Nowadays, people also include their streaming services,")
        print("for example Netflix, under utilities in lieu of what people")
        print("used to pay commonly for cable services.\n")

    elif data == "Food":
        print("\n\nFood and hygiene products\n")
        print("Groceries, personal care products, and things for baby needs")
        print("are expenses you’d include here. If you like to eat out a lot,")
        print("you might include those expenses here. But if eating out is")
        print("more something you do for fun, you can include it under")
        print("later category Personal & Discretionary\n")

    elif data == "Transportation":
        print("\n\nTransportation costs\n")
        print("The money you spend on public transit, taxis, fuel,")
        print("vehicle insurance, maintenance, and parking are included")
        print("in this category. This might change depending on whether")
        print("or not you’re working from home, but some should still")
        print("be allotted to understand your budget as a whole.\n")

    elif data == "Clothing":
        print("\n\nShoes and clothes for all members of the family.\n")

    elif data == "Medical":
        print("\n\nMedical\n")
        print("This includes premiums, specialists,")
        print("and over-the-counter medication.\n")

    elif data == "Personal & Discretionary":
        print("\n\nPersonal and discretionary spending\n")
        print("Money spent on entertainment, recreation, education,")
        print("tobacco & alcohol, eating out, gaming, hair cuts, hobbies,")
        print("and planned charitable giving are some examples. If you")
        print("spend more in this category, make sure your budget")
        print("balances by spending less elsewhere.\n")

    elif data == "Debt Payments":
        print("\n\nDebt payments\n")
        print("Many people find that their budget is quite tight when")
        print("their monthly debt payments are over 20% of their net")
        print("income. It’s good practice to save money before you")
        print("start heavily paying down your debt.\n")
        print("By following this basic plan and opening separate")
        print("accounts for different spending, as well as savings")
        print("accounts, you can more easily plan out your budget")
        print("percentages and work towards debt repayment.\n")

    elif data == "Boring savings":
        print("\n\nSavings: Emergency fund\n")
        print("If you already have saved up money in an emergency fund,")
        print("well done! You can enter 0 in this category.\n")
        print("If not, it is advised to dedicate savings towards this.")
        print("A general rule of thumb is to put away at least three to")
        print("six months’ worth of expenses for this.\n")

    elif data == "Fun savings":
        print("\n\nSavings: Fun!\n")
        print("This is savings that is purely for fun things.")
        print("For the purpose of this calculator, these savings")
        print("will be used to reach your specified goal.\n")


def validate_text(input):
    """
    Check text input to see if it meets the required criteria
    """
    # Check if input is empty
    if input == "":
        print('Invalid text: must enter a text.')
        return False

    return True


def validate_numbers(input):
    """
    Check number input to see if it meets the required critera
    """
    # Check if input is empty
    if input == "":
        print(f'\nInvalid data: must enter a number.')
        print('(Enter 0 if category is not applicable to you)\n')
        return False

    # Check if input is a number
    try:
        int(input)
    except ValueError:
        print(f'\nInvalid data: program can only process numbers.\n')
        return False

    # Check if input is a negative number
    if int(input) < 0:
        print(f'\nInvalid data: Program can not'
              'calculate with negative numbers\n')
        return False

    return True


def main():
    """
    Main function to call other function in the correct order
    """
    user = {}

    welcome()
    dream()
    goal(user)
    cost_of_goal = get_data(user, "Cost of goal")
    income = get_data(user, "Income")
    extra_income = get_data(user, "Extra income")
    housing = get_data(user, "Housing")
    utilities = get_data(user, "Utilities")
    food = get_data(user, "Food")
    transportation = get_data(user, "Transportation")
    clothing = get_data(user, "Clothing")
    medical = get_data(user, "Medical")
    personal_and_discretionary = get_data(user, "Personal & Discretionary")
    debt_payments = get_data(user, "Debt Payments")
    savings_emergency = get_data(user, "Boring savings")
    savings_fun = get_data(user, "Fun savings")
    print(user)


main()
