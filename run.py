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
  goal = input('Goal:\n')
  cost_of_goal = input('Estimate cost of goal:\n')

  user.update({"Goal": goal})
  user.update({"Cost of goal": cost_of_goal})
  return user


def get_income(user):
  """
  Ask user to input income data
  """
  income = input('Income:\n')
  validate_numbers(income)
  user.update({"Income": int(income)})
  return user


def get_expenses(user):
  """
  Ask user to input expenses data
  """
  expenses = input('Expenses:\n')
  user.update({"Expenses": int(expenses)})
  return user


def validate_numbers(input):
  """
  Check so that input is number and if it is not raise an error.
  """
  try:    
    [int(x) for x in input]
  except:
    print(f'\nInvalid data: program can only process numbers.')


def main():
  """
  Main function to call other function in the correct order
  """
  user = {"Goal": "",
          "Cost of goal": "",
          "Income": "",
          "Expenses": ""}
  
  welcome()
  dream()
  goal(user)
  get_income(user)
  get_expenses(user)
  print(user)


main()