import math
import pyfiglet
import sys
import time
import os
import signal


def welcome():
    """
    Start application on a welcome screen with a message
    """
    type_row_slow(big_heading_center('Dream'))
    time.sleep(0.5)
    type_row_slow(big_heading_center('Achiever'))
    time.sleep(1)

    type_text_slow('                Welcome to the DREAM ACHIEVER budget \
calculator!                \n              This tool will help you reach \
your dreams and goals.              ')
    time.sleep(0.6)

    type_row_fast('\n\n\nBudgeting Guidelines for Income:\n\n\
Many people wonder how much of their income they should spend on their home, \
\nvehicle, groceries, clothes, etc. At the end of this calculator we will \
compare \nyour expenses to the recommended guidelines and think about possible\
 changes you\ncan make.\n\nStart working with this budget calculator by \
developing your budget with your \nnet income. You have this money left \
after government deductions from your pay-\ncheque but before voluntary \
deductions like RRSPs, pensions, or other savings. \nIf you have expenses \
like high debt payments, childcare, school expenses, or \ngiving, you’ll need \
to lower your spending in your budgeting process in other \nareas to allow \
for these higher expenses.')

    type_text_slow('\n\nPress ENTER to continue...\n')
    input()


def dream():
    """
    Screen where user is asked to think about their dreams
    """
    type_row_slow(big_heading('Dream'))
    time.sleep(0.5)

    type_text_slow('First, let´s start with the fun stuff.\nImagine you won \
the lottery today!\n\n')
    time.sleep(1)
    type_text_slow('What would you do? Where would you go?\nWhat would your \
life look like?\n\n')
    time.sleep(1)
    type_text_slow('Take a few minutes and think about this.\n')

    type_text_slow('\n\nPress ENTER to continue...\n')
    input()


def goal(user):
    """
    Function to ask user to input a specific financial
    goal and estimate the cost of this goal
    """
    type_row_slow(big_heading('Goal'))
    time.sleep(0.5)

    type_row_fast('Okey, so this calculator will NOT help you win the \
lottery.\nHowever, we will begin a journey towards actualizing your dream.\n\
Take a part of your dream, one goal, the one thing that would bring you the\n\
best quality of life improvement right now. Could be for example getting away \
\non a vacation, just for relaxing or have an exciting adventure. Or moving to\
 a \nnew place. Or buying an expensive watch. One thing that is important to \
you.\n\nYou do not need to write any details here, can be just a keyword.\n\n')

    while True:

        goal = input('Goal:\n')
        if validate_text(goal):
            user.update({"Goal": goal})
            break

    get_data(user, "Cost of goal")


def intro_budget_calc():
    """
    Display information about the calculator to the user
    """
    type_row_fast(heading('\nBudget calculator'))

    type_row_fast('\nIt’s important to write everything out when planning your\
 financial goals, \nlike paying off your debt against your monthly income and \
fixed expenses. \nThis allows you to understand better where you are in your \
finances, as\nwell as help to plan out how you’re going to get where you want \
to be.\n\nThis calculator does not save any information from you.\n\nYou will \
be asked to enter data in the following categories:\nMain income, extra \
income, housing cost, utilities, food, \ntransportation, clothing, medical, \
personal & discretionary, \ndebt payments, boring savings and fun savings.\
\n\nA more detailed explanation of the category will be provided.\n')

    type_text_slow('\n\nPress ENTER to continue...\n')
    input()


def get_data(user, category):
    """
    Ask user to input data for income and expenses in each
    category and display a text explaining that category.
    """
    get_text(category)

    while True:

        data_input = input(f'{category}:\n')
        if validate_numbers(data_input):
            user.update({category: int(data_input)})
            break


def get_text(category):
    """
    Function to print different messages
    depending on the category of data input
    """
    if category == "Cost of goal":
        type_row_fast('\n\nEstimate the cost of your specified goal.\n\nYou do\
 not have to specify which currency your cost is in, but it is \nimportant \
to always stick to the same currency throughout the calculator. \nFor example,\
 if you live in Norway but have a salery in GBP and like to \norder german \
sausages online and pay in EUR then convert everything to \nwhichever \
currency is easiest or you.\n\n')

    elif category == "Income":
        type_row_fast(heading("\nMain income"))
        type_row_fast('\n\nEnter the amount from your main source of income \
here.\n\nFor the calculator to work properly, you need to enter your \nmonthly\
 income. Same goes for any extra income and for all costs. \nEstimate the \
average monthly on each category.\n\n')

    elif category == "Extra income":
        type_row_fast(heading('\nExtra income'))
        type_row_fast('\n\nFor example, this could be income from commissions,\
 overtime, \nbonuses, rent (recieved), child support, benefits etc.\n\n')

    elif category == "Housing":
        type_row_fast(heading('\nHousing costs'))
        type_row_fast('\n\nThis would include mortgage payments, property \
taxes, strata fees, \nrent, homeowner insurance, and hydro or electricity.\
\n\n')

    elif category == "Utilities":
        type_row_fast(heading('\nUtilities'))
        type_row_fast('\n\nExamples of utility costs are cell phone, gas, and \
internet\nbills. Nowadays, people also include their streaming services,\n\
for example Netflix, under utilities in lieu of what people\n\
used to pay commonly for cable services.\n\n')

    elif category == "Food":
        type_row_fast(heading('\nFood and hygiene products'))
        type_row_fast('\n\nGroceries, personal care products, and things for \
baby needs\nare expenses you’d include here. If you like to eat out a lot,\n\
you might include those expenses here. But if eating out is\nmore something \
you do for fun, you can include it under later \n\
category Personal & Discretionary\n\n')

    elif category == "Transportation":
        type_row_fast(heading('\nTransportation costs'))
        type_row_fast('\n\nThe money you spend on public transit, taxis, fuel,\
\nvehicle insurance, maintenance, and parking are included\nin this category. \
This might change depending on whether\nor not you’re working from home, but \
some should still\nbe allotted to understand your budget as a whole.\n\n')

    elif category == "Clothing":
        type_row_fast(heading('\nClothing'))
        type_row_fast('\n\nShoes and clothes for all members of the family.\
\n\n')

    elif category == "Medical":
        type_row_fast(heading('\nMedical'))
        type_row_fast('\n\nThis includes premiums, specialists,\n\
and over-the-counter medication.\n\n')

    elif category == "Personal & Discretionary":
        type_row_fast(heading('\nPersonal & Discretionary'))
        type_row_fast('\n\nMoney spent on entertainment, recreation, \
education,\ntobacco & alcohol, eating out, gaming, hair cuts, hobbies,\n\
and planned charitable giving are some examples.\n\n')

    elif category == "Debt Payments":
        type_row_fast(heading('\nDebt Payments'))
        type_row_fast('\n\nHere you can enter the monthly payments on various \
debts.\nCould be for example credit card debt or loan for a car.\n\n')

    elif category == "Boring savings":
        type_row_fast(heading('\nBoring savings'))
        type_row_fast('\n\nIf you already have saved up money in an emergency \
fund,\nwell done! If not, it is advised to dedicate savings towards\nthis. \
It is also a good idea to have some savings set aside\nfor retirement. This \
category could also include savings for\ngrandchildren or any other types of \
long term savings.\n\n')

    elif category == "Fun savings":
        type_row_fast(heading('\nFun savings'))
        type_row_fast('\n\nThis is savings that is purely for fun things. \n\
For the purpose of this calculator, these savings\nwill be used to reach your \
specified goal.\n\n')

    elif category == "Initial savings":
        type_row_fast(heading('\nInitial savings'))
        type_row_fast('\n\nDo you already have any amount of savings that \n\
you want to dedicate towards reaching your goal?\n\
If you do not, that is fine, just enter 0.\n\n')


def collect_data(user):
    """
    Iterate through a list of categories to run a
    function to collect data from user in each category
    """
    categories = ["Income", "Extra income", "Housing", "Utilities", "Food",
                  "Transportation", "Clothing", "Medical",
                  "Personal & Discretionary", "Debt Payments",
                  "Boring savings", "Fun savings", "Initial savings"]

    for category in categories:
        get_data(user, category)


def validate_text(input):
    """
    Check text input to see if it meets the required criteria
    """
    # Check if input is empty
    if input == "":
        print('Invalid text: must enter a text.')
        return False

    # Check if input has more than 60 characters
    if len(input) > 60:
        print('Invalid text: must be less 60 characters or less.')
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

    # Check if input has more than 60 characters
    if len(input) > 20:
        print(f'\nInvalid data: number must be 20 characters or less.')
        return False

    return True


def calc_budget_surplus(user, income):
    """
    Function to compare income with cost to see
    if there is a budget surplus avalible
    """
    # Get values from user and slice list to get the costs and sum them up
    costs = list(user.values())[4:-1]
    expenses = 0
    for cost in costs:
        expenses += cost

    budget_surplus = income - expenses

    # Print different messages based on the value of the budget surplus
    if budget_surplus < 0:
        type_text_slow(f'\n\nLooks like your budget exceeds your income with \
{budget_surplus},\nwe will have to deduct this from your fun savings for now.')

    elif budget_surplus > 0:
        type_text_slow(f'\n\nGreat, you have a budget surplus of \
{budget_surplus},\nwe will use this money towards reaching your goal.')

    else:
        type_text_slow(f'\n\nLooks like somebody did their homework and came \
prepared, well done!\nYour income ({income}) and expenses ({expenses}) \
are the same amount.\n')

    return budget_surplus


def calculate_goal(user, surplus):
    """
    Compare users goal to the fun savings -+ budget surplus
    and check how long it will take to reach this goal
    """
    # Get required values for calculation
    goal_cost = list(user.values())[1]
    fun_savings = list(user.values())[-2]
    initial_savings = list(user.values())[-1]

    # Check avalible monthly savings that can be used towards reaching goal
    goal_funds = fun_savings + surplus
    if goal_funds <= 0:
        reach_goal = 0  # number of months to reach goal
    else:
        reach_goal = (goal_cost - initial_savings) / goal_funds

    # Check if user can already afford their goal
    if initial_savings >= goal_cost:
        type_text_slow('\n\nGood news, you already have enough savings to \
reach your goal!')
    else:
        # Function to display time to reach goal in nr of years if applicable
        years = 0
        months = 0

        # If months is higher than 12, display time in years and months
        if reach_goal > 12:
            years = reach_goal / 12
            years = math.floor(years)
            months = math.ceil(reach_goal) - (years * 12)
            # prevent from displaying for example "2 years and 12 months"
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
        # do not display year/years/and at all if less than 1 year
        if years == 0:
            years = ""
            years_text = ""
            and_text = ""

        # do not display and/months or the word and if less than 1 month
        if months == 0:
            months = ""
            months_text = ""
            and_text = ""

        time.sleep(0.8)
        type_text_slow(f'\n\nYour goal is: "{list(user.values())[0]}"\nand \
your current savings towards your goal is {goal_funds} per month.')

        time.sleep(0.8)

        # Message if there is no avalible savings towards goal
        if goal_funds <= 0:
            type_text_slow('\n\nAt this point, you will not be able to reach \
your goal.')

        # Message if there it takes more than 20 years to reach goal
        elif reach_goal > 240:
            type_text_slow(f'\n\nAt this rate it will take you over 20 years \
to reach your goal. \nSpecifically {years}{years_text}{and_text}\
{months}{months_text}.')

        # Message if there is avalible savings and goal will be reached
        else:
            type_text_slow(f'\n\nIt will take you {years}{years_text}\
{and_text}{months}{months_text} to reach your goal.\n')
            time.sleep(0.8)
            type_text_slow('If you want to reach this goal faster you can to \
either cut\nsome of your other expenses, try to increase your income or\n\
find some new extra income.')

    time.sleep(1)
    type_text_slow('\n\nLet´s look through your expenses and \
think about ways to reduce them.\n')

    type_text_slow('\n\nPress ENTER to continue...\n')
    input()


def get_cost_text(category):
    """
    Function to print different messages
    depending on the category of cost
    """
    guideline_percent = 0

    if category == "Housing":
        type_row_fast(heading('\nHousing'))
        type_row_fast('\n\nOther than moving to a cheaper place, there are \
many small things you can do to\nreduce your living costs. For example it is \
a good idea to regularly check what\nthe best avalible interest rate on your \
mortgage. Also compare offers from\ndifferent companies on for example \
insurance and electricity.')

        guideline_percent = 35

    elif category == "Utilities":
        type_row_fast(heading('\nUtilities'))
        type_row_fast('\n\nComparing offers from different providers can save \
costs.\nLimiting the amount of different streaming services you \n\
subscribe to at the same time can make a big impact too.')

        guideline_percent = 5

    elif category == "Food":
        type_row_fast(heading('\nFood and hygiene products'))
        type_row_fast('\n\nThere are many ways to cut down on food costs, \
from where you do your grocery\nshopping to what you choose to eat. Can also \
be a good idea to take advantage\nof coupon deals and special prices avalible \
in the store.')

        guideline_percent = 15

    elif category == "Transportation":
        type_row_fast(heading('\nTransportation'))
        type_row_fast('\n\nTransportation needs varies a lot depending on \
for example family\ncircumstances or where you live and work. In some \
situations public \ntransportation will be a cheaper option. Walking and \
riding bicycle´s\nare cheap alternatives while also having the added benefit \
getting \nmore exercise and it is environmentally friendly.')

        guideline_percent = 17

    elif category == "Clothing":
        type_row_fast(heading('\nClothing'))
        type_row_fast('\n\nUse shoes and clothes for a longer period of time\n\
before replacing to cut costs in this category.\nCan also look into \
buying second hand items.')

        guideline_percent = 4

    elif category == "Medical":
        type_row_fast(heading('\nMedical'))
        type_row_fast('\n\nHard cost to try and cut, if you need it you need \
it. Some studies \nsay that a healthy lifestyle can reduce future \
medical costs.')

        guideline_percent = 3

    elif category == "Personal & Discretionary":
        type_row_fast(heading('\nPersonal & Discretionary'))
        type_row_fast('\n\nThe content for this category will vary much from \
person to person depending\non circumstances. If you spend more in this \
category, make sure your budget\nbalances by spending less elsewhere.')

        guideline_percent = 7.5

    elif category == "Debt Payments":
        type_row_fast(heading('\nDebt Payments'))
        type_row_fast('\n\nMany people find that their budget is quite tight \
when their monthly debt\npayments are over 20% of their net income. It’s good \
practice to save money\nbefore you start heavily paying down your debt.\n\n\
By following this basic plan and opening separate accounts for different\n\
spending, as well as savings accounts, you can more easily plan out your\n\
budget percentages and work towards debt repayment.')

        guideline_percent = 10

    elif category == "Boring savings":
        type_row_fast(heading('\nBoring savings'))
        type_row_fast('\n\nA general rule of thumb is to put away at least \
three to six months’ worth of\nexpenses in an emergency fund. It is also \
advised to start saving up for your\nretirement as early as possible. How \
much you need for this is depending on\nwhat other pension plans or \
workplace pension you have already.')

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
        # Only display decimals if % is below 10
        if percent_of_income > 10:
            percent_of_income = round(percent_of_income)

    # Change text depending on if budget is below, above or same as guideline
    comparason = ""
    if guideline_percent > percent_of_income:
        comparason = "below this at"
    elif guideline_percent < percent_of_income:
        comparason = "above this at"
    else:
        comparason = "also"

    type_row_fast(f'\n\nGeneral guidelines to spend in this category is \
{guideline_percent}% of your total income.')
    if income == 0:
        # Message IF user filled in income as 0
        type_row_fast('\nUnable to calculate you % since your income is: 0.')
    else:
        type_row_fast(f'\nYour budget for this is currently \
{comparason} {percent_of_income}%.')

    type_row_fast('\n\nPress ENTER to continue...\n')
    input()


def run_calculations(user):
    """
    Run all calculations to check if there is a budget surplus
    and check how long it will take to reach the specified goal.
    Then iterate through the categories to print text on each
    category and compare budgets with the general recommendation.
    """
    type_row_slow('\n\n')
    type_text_slow('Calculating.........................')

    # Add income's together to use in other calculations
    income = user.get("Income") + user.get("Extra income")

    budget_surplus = calc_budget_surplus(user, income)
    calculate_goal(user, budget_surplus)

    categories = ["Housing", "Utilities", "Food", "Transportation",
                  "Clothing", "Medical", "Personal & Discretionary",
                  "Debt Payments", "Boring savings"]

    for category in categories:
        check_costs(user, income, category)


def thank_you():
    """
    Thank the user for using the calculator and give another helpful tip
    """
    type_row_fast(big_heading('\nThank'))
    type_text_slow('you for using our budget calculator!\nWe hope this helped \
you to think about your expenses and also clarify your\ndreams and goals. \
This is the first step needed towards achieving them.\n')

    time.sleep(0.8)
    type_row_fast('\n\nWould you like to learn about another helpful tip you \
can use when\nplanning your budget? It is called the 50-30-20 rule.\n')

    # Run function ask question with the question and valid responses
    responses = ["Yes", "yes", "YES", "Y", "y", "No", "no", "NO", "N", "n"]
    question = 'Answer with "Yes" or "No"'

    response = ask_question(responses, question)

    # If user chooses a variation of Yes, display recommendation, else continue
    if response in responses[0:5]:
        another_recommendation()
    else:
        start_over()


def another_recommendation():
    """
    Give another helpful tip if user chooses to learn it
    """
    type_row_fast(big_heading_center('\n50-30-20'))
    type_row_fast('The 50-30-20 rule splits expenses into just three \
categories. It also offers\nrecommendations on how much money to use for \
each. With some basic information,\nyou can get on the road to financial \
well-being.')

    type_row_fast('\n\nPress ENTER to continue...\n')
    input()

    type_row_fast(heading('\nNeeds: 50%'))
    type_row_fast('\n\nAbout half of your budget should go toward needs. These\
 are expenses\nthat must be met no matter what, for example rent/mortgage \
payments,\nminimum payments on loans, healthcare, and essential groceries.')

    type_row_fast('\n\nPress ENTER to continue...\n')
    input()

    type_row_fast(heading('\nWants: 30%'))
    type_row_fast('\n\nYou subscribe to a streaming service to watch your \
favorite show, not\nbecause you need the subscription to live. Wants are \
things you enjoy\nthat you spend money on by choice. This could be \
subscriptions,\nsupplies for hobbies, restaurant meals and vacations.')

    type_row_fast('\n\nPress ENTER to continue...\n')
    input()
    type_row_fast(heading('\nSavings: 20%'))

    type_row_fast('\n\nThe remaining 20% of your budget should go toward the \
future. You may put money\nin an emergency fund, or save toward a down \
payment on a home. Paying down debt\nbeyond the minimum payment amount \
belongs in this category, too.')

    type_row_fast('\n\nPress ENTER to continue...\n')
    input()

    start_over()


def start_over():
    """
    Give user the option to start calculator over again
    """
    type_row_fast(big_heading('\nDream'))
    type_row_fast('Would you like to start over with another calculation?\n\n')

    # Run function ask question with the question and valid responses
    responses = ["Yes", "yes", "YES", "Y", "y", "No", "no", "NO", "N", "n"]
    question = 'Answer with "Yes" or "No"'

    response = ask_question(responses, question)

    # If user chooses a variation of Yes, start over, else continue
    if response in responses[0:5]:
        main()
    else:
        good_bye()


def good_bye():
    """
    Say good bye to user
    """
    type_row_fast(big_heading('\nGood bye'))
    type_row_fast('Hope you had a pleasant experience and good luck\nreaching \
all of your dreams and goals!\n\nIf you changed your mind and want to do \
another calculation\nclick on "Run program" button above.\n\nHave a nice day!')
    sys.exit()


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
    Validate the response and give feedback to user if wrong
    """
    if response not in responses:
        print('Sorry, I do not understand what you mean.')
        return False

    return True


def type_text_slow(message):
    """
    Function to write text slowly to terminal,
    character by character on a timer
    """
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def type_row_slow(message):
    """
    Function to write text slowly to terminal,
    row by row on a timer
    """
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        if character == "\n":
            time.sleep(0.3)


def type_row_fast(message):
    """
    Function to write text slowly to terminal,
    row by row on a timer
    """
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        if character == "\n":
            time.sleep(0.02)


def big_heading_center(text):
    """
    Function to create a big centered heading
    """
    heading = pyfiglet.figlet_format(text, font="big_money-se",
                                     justify="center")

    return heading


def big_heading(text):
    """
    Function to create a big heading
    """
    heading = pyfiglet.figlet_format(text, font="big_money-se")

    return heading


def heading(text):
    """
    Function to create a heading
    """
    text = text.upper()
    heading = pyfiglet.figlet_format(text, font="digital")

    return heading


def handler(signum, frame):
    """
    Custom message when user presses Ctrl-c instead of error.
    """
    type_text_slow('\nCtrl-c was pressed, terminating program.\n')
    type_row_fast(big_heading('Good bye'))
    sys.exit()


def main():
    """
    Main function to call functions in the correct order
    """
    # define user as empty dictionary
    user = {}

    # used to catch ctrl-c click
    signal.signal(signal.SIGINT, handler)

    welcome()
    dream()
    goal(user)
    intro_budget_calc()
    collect_data(user)
    run_calculations(user)
    thank_you()


main()
