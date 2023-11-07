# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def welcome():
  """
  Start application on a welcome screen with a message
  """
  print('\nWelcome message\n')
  print('Press ENTER to continue')


def dream():
  """
  Screen where user think about their dreams
  """
  print('Dream')


def goal():
  """
  Function to ask user to input a specific financial goal
  """
  print('Goal')


def main():
  """
  Main function to call other function in the correct order
  """
  welcome()
  dream()
  goal()


main()