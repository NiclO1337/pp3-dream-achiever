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
    while True:

        data_input = input(f'{data}:\n')
        if validate_numbers(data_input):
            user.update({data: int(data_input)})
            return user


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
        print('\nInvalid data: Program can not calculate with negative numbers\n')
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
    expenses = get_data(user, "Expenses")
    print(user)


main()
