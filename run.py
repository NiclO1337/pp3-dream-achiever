import math
import pyfiglet
import sys
import time
import os


def welcome():
    """
    Start application on a welcome screen with a message
    """
    dream_heading = pyfiglet.figlet_format('Dream',
                                           font="big_money-se",
                                           justify="center")

    type_row_slow(dream_heading)    

    time.sleep(0.5)

    achiever_heading = pyfiglet.figlet_format('Achiever',
                                 font="big_money-se",
                                 justify="center")

    type_row_slow(achiever_heading)
    
    time.sleep(1)

    welcome = '             Welcome to the DREAM ACHIEVER budget calculator!\n\
           This tool will help you reach your dreams and goals.'

    type_text_slow(welcome)

    time.sleep(1)


    
#     print()
#     print()
#     print()
#     print()
#     print('\nWelcome to the DREAM ACHIEVER budget calculator!\n'
#           'This tool will help you reach your dreams and goals.\n')
#     print('Budgeting Guidelines for Income:')
#     print('Many people wonder how much of their income they should spend on '
#           'their home, vehicle, groceries, clothes, etc. At the end of this '
#           'calculator we will compare your expenses to the recommended '
#           'guidlines and think about possible changes you can make.\n'
#           'Start working with this budget calculator by developing your \
# budget with your net income. You have this money left after '
#           'government deductions from your paycheque but before voluntary '
#           'deductions like RRSPs, pensions, or other savings. If you have '
#           'expenses like high debt payments, childcare, school expenses, or '
#           'giving, you’ll need to lower your spending in your budgeting '
#           'process in other areas to allow for these higher expenses.')

#     input('\nPress ENTER to continue...\n')


def dream():
    """
    Screen where user think about their dreams
    """
    print('\nDream\n')
    print('First, let´s start with the fun stuff.\n'
          'Imagine you won the lottery today!\n'
          '\nWhat would you do? Where would you go?\n'
          'What would your life look like?\n'
          '\nTake a few minutes and think about this.\n')

    input('Press ENTER to continue...\n')


def goal(user):
    """
    Function to ask user to input a specific financial goal
    """
    print('\nGoal\n')
    print('Okey, so this calculator will NOT help you win the lottery.\n'
          'However, we will begin a journey towards actualizing your dream.\n'
          'Take a part of your dream, one goal, the one thing that would '
          'bring you the best quality of life improvement right now. '
          'Could be for example getting away on a vacation, just for relaxing '
          'or have an exciting adventure. Or moving to a new place. '
          'Or buying an expensive watch. One thing that is important to you.')
    print('\nYou do not need to write any details here, '
          'can be just a keyword.')

    while True:

        goal = input('Goal:\n')
        if validate_text(goal):
            user.update({"Goal": goal})
            return user


def introduction():
    """
    Displays information about the calculator
    """
    print('\n\nBudget calculator\n')
    print('It’s important to write everything out when planning your financial'
          ' goals, like paying off your debt against your monthly income and '
          'fixed expenses. This allows you to understand better where you are '
          'in your finances, as well as help to plan out how '
          'you’re going to get where you want to be.\n')
    print('This calculator does not save any information from you.\n'
          'Good news, your privacy is protected. Bad news, you can not revisit'
          ' the results of this calculator after you leave or reset.\n'
          'You will be asked to enter data in the following categories:\n'
          'Main income, extra income, housing cost, utilities, food,'
          'transportation, clothing, medical, personal & discretionary, '
          'debt payments, boring savings and fun savings.\n'
          '\nA more detailed explanation of the category will be provided.\n')

    input('Press ENTER to continue...\n')


def get_data(user, data):
    """
    Ask user to input data for income
    and expenses in each category
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
        print('\n\nEstimate the cost of your specified goal.\n')
        print('You do not have to specify which currency your cost is in,')
        print('but it is important to always stick to the same currency')
        print('throughout the calculator.')
        print('For example, if you live in Norway but have a salery in GBP')
        print('and like to order german sausages online and pay in EUR then ')
        print('convert everything to whichever currency is easiest or you.\n')

    elif data == "Income":
        print('\n\nMain income\n')
        print('Enter the amount from your main source of income here.\n')
        print('For the calculator to work properly, you need to enter your '
              'monthly income. Same goes for any extra income and for all '
              'costs. Estimate the average monthly on each category.\n')

    elif data == "Extra income":
        print('\n\nExtra income\n')
        print('For example, this could be income from commissions, overtime, '
              'bonuses, rent (recieved), child support, benefits etc.\n')

    elif data == "Housing":
        print('\n\nHousing costs\n')
        print('This would include mortgage payments, property taxes, strata')
        print('fees, rent, homeowner insurance, and hydro or electricity.\n')

    elif data == "Utilities":
        print('\n\nUtilities\n')
        print('Examples of utility costs are cell phone, gas, and internet')
        print('bills. Nowadays, people also include their streaming services,')
        print('for example Netflix, under utilities in lieu of what people')
        print('used to pay commonly for cable services.\n')

    elif data == "Food":
        print('\n\nFood and hygiene products\n')
        print('Groceries, personal care products, and things for baby needs')
        print('are expenses you’d include here. If you like to eat out a lot,')
        print('you might include those expenses here. But if eating out is')
        print('more something you do for fun, you can include it under')
        print('later category Personal & Discretionary\n')

    elif data == "Transportation":
        print('\n\nTransportation costs\n')
        print('The money you spend on public transit, taxis, fuel,')
        print('vehicle insurance, maintenance, and parking are included')
        print('in this category. This might change depending on whether')
        print('or not you’re working from home, but some should still')
        print('be allotted to understand your budget as a whole.\n')

    elif data == "Clothing":
        print('\n\nShoes and clothes for all members of the family.\n')

    elif data == "Medical":
        print('\n\nMedical\n')
        print('This includes premiums, specialists,')
        print('and over-the-counter medication.\n')

    elif data == "Personal & Discretionary":
        print('\n\nPersonal and discretionary spending\n')
        print('Money spent on entertainment, recreation, education,')
        print('tobacco & alcohol, eating out, gaming, hair cuts, hobbies,')
        print('and planned charitable giving are some examples.\n')

    elif data == "Debt Payments":
        print('\n\nDebt payments\n')
        print('Here you can enter the monthly payments on various debts.')
        print('Could be for example credit card debt or loan for a car.\n')

    elif data == "Boring savings":
        print('\n\nBoring savings\n')
        print('If you already have saved up money in an emergency fund,')
        print('well done! If not, it is advised to dedicate savings towards')
        print('this. It is also a good idea to have some savings set aside')
        print('for retirement. This category could also include savings for')
        print('grandchildren or any other types of long term savings.\n')

    elif data == "Fun savings":
        print('\n\nSavings: Fun goal!\n')
        print('This is savings that is purely for fun things.')
        print('For the purpose of this calculator, these savings')
        print('will be used to reach your specified goal.\n')

    elif data == "Initial savings":
        print('\n\nInitial savings\n')
        print('Do you already have any amount of savings that')
        print('you want to dedicate towards reaching your goal.')
        print('If you do not, that is okey, just enter 0\n')


def collect_data(user):
    """
    Collect data from user
    """
    get_data(user, "Income")
    get_data(user, "Extra income")
    get_data(user, "Housing")
    get_data(user, "Utilities")
    get_data(user, "Food")
    get_data(user, "Transportation")
    get_data(user, "Clothing")
    get_data(user, "Medical")
    get_data(user, "Personal & Discretionary")
    get_data(user, "Debt Payments")
    get_data(user, "Boring savings")
    get_data(user, "Fun savings")
    get_data(user, "Initial savings")


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
        print(f'\nInvalid data: Program can not '
              'calculate with negative numbers.\n')
        return False

    return True


def compare_income_cost(user, income):
    """
    Function to compare income with cost to see
    if there is a budget surplus avalible
    """
    # Get values from user and slice list to get the costs
    costs = list(user.values())[4:-1]
    expenses = 0
    for cost in costs:
        expenses += cost

    budget_surplus = income - expenses

    # Print different messages based on the value of the budget surplus
    if budget_surplus < 0:
        print('\n\nLooks like your budget exceeds your income with '
              f'{budget_surplus}, we will have to deduct this from '
              'your fun savings for now.\n')
    elif budget_surplus > 0:
        print(f'\n\nGreat, you have a budget surplus of {budget_surplus}, '
              'we will use this money towards reaching your goal.\n')
    else:
        print('\n\nLooks like somebody did their homework and came prepared, '
              f'well done! Your income ({income}) and expenses ({expenses}) '
              'are the same amount.\n')

    return budget_surplus


def calculate_goal(user, surplus):
    """
    Compare users goal to the fun savings -+ budget surplus
    and check how long it will take to reach this goal
    """

    goal_cost = list(user.values())[1]
    fun_savings = list(user.values())[-2]
    initial_savings = list(user.values())[-1]
    goal_funds = fun_savings + surplus
    if goal_funds <= 0:
        reach_goal = 0
    else:
        reach_goal = (goal_cost - initial_savings) / goal_funds

    # Check if user can already afford their goal
    if initial_savings >= goal_cost:
        print('Good news, you already have enough savings to reach your goal!')
    else:
        # Function to display time to reach goal in nr of years if applicable
        years = 0
        months = 0

        # If months is higher than 12, display time in years and months
        if reach_goal > 12:
            years = reach_goal / 12
            years = math.floor(years)
            months = math.ceil(reach_goal) - (years * 12)
            if months == 12:
                years += 1
                months = 0

        # If months is 12 or less, only display months and not years
        if reach_goal <= 12:
            months = math.ceil(reach_goal)

        # correctly display time as "year" or "years" in print message
        years_text = " year"
        months_text = " month"
        and_text = " and "

        if years > 1:
            years_text = " years"

        if months > 1:
            months_text = " months"
        # do not display year/years at all if less than 1 year
        if years == 0:
            years = ""
            years_text = ""
            and_text = ""

        # do not display months or the word and if months = 0
        if months == 0:
            months = ""
            months_text = ""
            and_text = ""

        print(f'Your goal is: "{list(user.values())[0]}" and your current '
              f'savings towards your goal is {goal_funds} per month.')

        if goal_funds <= 0:
            print('At this point, you will not be able to reach your goal.')

        elif reach_goal > 240:
            print('At this rate it will take you over 20 years to reach your '
                  f'goal. Specifically {years}{years_text}{and_text}'
                  f'{months}{months_text}.')

        else:
            print(f'It will take you {years}{years_text}'
                  f'{and_text}{months}{months_text} to reach your goal. '
                  'If you want to reach this goal faster you can to either '
                  'cut some of your other expenses, try to increase your '
                  'income or find some new extra income.')

    print('\nLet´s look through your expenses and '
          'think about ways to reduce them.\n')

    input('Press ENTER to continue...\n')


def get_cost_text(category):
    """
    Function to print different messages
    depending on the category of cost
    """
    guideline_percent = 0

    if category == "Housing":
        print('\n\nHousing costs\n')
        print('Other than moving to a cheaper place, there are many small '
              'things you can do to reduce your living costs. For example it '
              'is a good idea to regularly check what the best avalible '
              'interest rate on your mortgage. Comparing offers from '
              'different companies on for example insurance and electricity '
              'can save a lot of money. ')

        guideline_percent = 35

    elif category == "Utilities":
        print('\n\nUtilities\n')
        print('Comparing offers from different providers can save costs. '
              'Limiting the amount of different streaming services you '
              'subscribe to at the same time can make a big impact too.')

        guideline_percent = 5

    elif category == "Food":
        print('\n\nFood and hygiene products\n')
        print('There are many ways to cut down on food costs, from where '
              'you do your grocery shopping to what you choose to eat. '
              'Can also be a good idea to take advantage of coupon deals '
              'and special prices avalible in the store.')

        guideline_percent = 15

    elif category == "Transportation":
        print('\n\nTransportation costs\n')
        print('Transportation needs are very different for example based on '
              'family circumstances or where you live and work. In some '
              'situations public transportation will be a cheaper option. '
              'Walking and riding bicycle´s are cheap alternatives while also '
              'having the added benefit getting more exercise and it is '
              'environmentally friendly.')

        guideline_percent = 17.5

    elif category == "Clothing":
        print('\n\nShoes and clothes for all members of the family.\n')
        print('Use shoes and clothes for a longer period of time before '
              'replacing to cut costs in this category. Can also look into '
              'buying second hand items.')

        guideline_percent = 4

    elif category == "Medical":
        print('\n\nMedical\n')
        print('Hard cost to try and cut, if you need it you need it. '
              'Some studies say that a healthy lifestyle can reduce '
              'future medical costs.')

        guideline_percent = 3

    elif category == "Personal & Discretionary":
        print('\n\nPersonal and discretionary spending\n')
        print('The content for this category will vary much from person to '
              'person depending on circumstances. If you spend more in this '
              'category, make sure your budget balances by '
              'spending less elsewhere.')

        guideline_percent = 7.5

    elif category == "Debt Payments":
        print('\n\nDebt payments\n')
        print('Many people find that their budget is quite tight when')
        print('their monthly debt payments are over 20% of their net')
        print('income. It’s good practice to save money before you')
        print('start heavily paying down your debt.\n')
        print('By following this basic plan and opening separate')
        print('accounts for different spending, as well as savings')
        print('accounts, you can more easily plan out your budget')
        print('percentages and work towards debt repayment.')

        guideline_percent = 10

    elif category == "Boring savings":
        print('\n\nBoring saving\n')
        print('A general rule of thumb is to put away at least three to six '
              'months’ worth of expenses in an emergency fund. It is also '
              'advised to start saving up for your retirement as early as '
              'possible. How much you need for this is depending on what '
              'other pension plans or workplace pension you have already.')

        guideline_percent = 10

    return guideline_percent


def check_costs(user, income, category):
    """
    Function to compare costs to the recommended values
    and write budget recommendation to user
    """
    # Get text associated with each category and get the guideline percentage
    guideline_percent = get_cost_text(category)

    # Convert user budget to percentage with 2 decimals
    if income == 0:
        percent_of_income = 0
    else:
        percent_of_income = round((user.get(category) / income * 100), 2)

    # Change text depending on if budget is below, above or same as guideline
    comparason = ""
    if guideline_percent > percent_of_income:
        comparason = "below this at"
    elif guideline_percent < percent_of_income:
        comparason = "above this at"
    else:
        comparason = "also"

    print('\nGeneral guidelines to spend in this category is '
          f'{guideline_percent}% of your total income.')
    if income == 0:
        print('Unable to calculate you % since your income is set to 0.')
    else:
        print('Your budget for this is currently '
              f'{comparason} {percent_of_income}%.')

    input('\nPress ENTER to continue...')


def run_calculations(user):
    """
    Run all calculations to check if there is a budget surplus
    and check how long it will take to reach the specified goal.
    Then compares each category of costs with the general recommendation.
    """
    # Add income's together to use in other calculations
    income = user.get("Income") + user.get("Extra income")

    budget_surplus = compare_income_cost(user, income)
    calculate_goal(user, budget_surplus)

    check_costs(user, income, "Housing")
    check_costs(user, income, "Utilities")
    check_costs(user, income, "Food")
    check_costs(user, income, "Transportation")
    check_costs(user, income, "Clothing")
    check_costs(user, income, "Medical")
    check_costs(user, income, "Personal & Discretionary")
    check_costs(user, income, "Debt Payments")
    check_costs(user, income, "Boring savings")


def thank_you():
    """
    Thank the user for using the calculator and give another helpful tip
    """
    print('\n\nThank you')
    print('for using our budget calculator!\nWe hope this helped you '
          'to think about your expenses and also clarify your dreams and '
          'goals. This is the first step needed towards achieving them.\n')
    print('Would you like to learn about another helpful tip you can use '
          'when plannin your budget? It is called the 50-30-20 rule.\n')

    responses = ["Yes", "yes", "YES", "Y", "y", "No", "no", "NO", "N", "n"]
    question = 'Answer with "Yes" or "No"'

    response = ask_question(responses, question)

    if response in responses[0:5]:
        another_recommendation()
    else:
        start_over()


def another_recommendation():
    """
    Give another helpful tip if user chooses to learn it
    """
    print('The 50-30-20 Rule\n')
    print('The 50-30-20 rule splits expenses into just three categories. It '
          'also offers recommendations on how much money to use for each. '
          'With some basic information, you can get on the road to financial '
          'well-being.\n')

    input('\nPress ENTER to continue...\n')

    print('Needs: 50%\nAbout half of your budget should go toward needs. '
          'These are expenses that must be met no matter what, for example '
          'rent/mortgage payments, minimum payments on loans, healthcare, '
          'and groceries.\n')

    print('Wants: 30%\nYou subscribe to a streaming service to watch your '
          'favorite show, not because you need the subscription to live. '
          'Wants are things you enjoy that you spend money on by choice. '
          'This could be subscriptions, supplies for hobbies, restaurant '
          'meals and vacations.\n')

    print('Savings: 20%\nThe remaining 20% of your budget should go toward '
          'the future. You may put money in an emergency fund, or save toward '
          'a down payment on a home. Paying down debt beyond the minimum '
          'payment amount belongs in this category, too.')

    input('\nPress ENTER to continue...\n')

    start_over()


def start_over():
    """
    Give user the option to start calculator over again
    """
    print('Dream achiever')
    print('Would you like to start over with another calculation?')

    responses = ["Yes", "yes", "YES", "Y", "y", "No", "no", "NO", "N", "n"]
    question = 'Answer with "Yes" or "No"'

    response = ask_question(responses, question)

    if response in responses[0:5]:
        main()
    else:
        good_bye()


def good_bye():
    """
    Say good bye to user
    """
    print('Good bye')
    print('Hope you had a pleasant experience and good luck reaching '
          'all of your dreams and goals!')
    print('\nIf you changed your mind and want to do another calculation '
          'click on "Run program" button above.\n\n'
          'Have a nice day!')


def ask_question(responses, question):
    """
    Function that asks user to answer a question and
    return the response. Keep asking until the answer matches
    one of the valid options in the responses list.
    """
    while True:

        response = input(f'{question}:\n')
        if validate_response(response, responses):
            break

    return response


def validate_response(response, responses):
    """
    Validate the the response and give feedback to user if wrong
    """
    if response not in responses:
        print('Sorry, I do not understand what you mean.')
        return False

    return True


def type_text_slow(message):
    """
    Function to write text slowly to terminal
    """
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    
def type_row_slow(message):
    """
    Function to write text slowly to terminal
    """
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        if character == "\n":
            time.sleep(0.3)


def main():
    """
    Main function to call other function in the correct order
    """
    user = {}

    # user = {"Goal": "Trip to the Bahamas",
    #         "Cost of goal": 50000,
    #         "Income": 23000,
    #         "Extra income": 10000,
    #         "Housing": 14000,
    #         "Utilities": 1500,
    #         "Food": 5000,
    #         "Transportation": 150,
    #         "Clothing": 200,
    #         "Medical": 150,
    #         "Personal & Discretionary": 7000,
    #         "Debt Payments": 0,
    #         "Boring savings": 4000,
    #         "Fun savings": 2000,
    #         "Initial savings": 10000}

    welcome()
    # dream()
    # goal(user)
    # get_data(user, "Cost of goal")
    # introduction()
    # collect_data(user)
    # run_calculations(user)
    # thank_you()


main()
