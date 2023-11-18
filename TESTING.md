
# Dream Achiever

![Amiresponsive image](https://res.cloudinary.com/dmntcacug/image/upload/v1700167217/Amiresponsive_nl4tfn.png)


Link to live website: [Dream Achiever](https://dream-achiever-3a6af54c4f68.herokuapp.com/) <br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)

<hr>

## Table of contents

TODO: Update table of content

* [Testing](#testing)
    * [Automatic testing](#automatic-testing)
    * [Manual testing](#manual-testing)
        * [User goals](#user-goals)
        * [Features](#features)
        * [Browser](#browser)
    * [Bugs](#bugs)
        * [Solved bugs](#solved-bugs)
        * [Unfixed bugs](#unfixed-bugs)



## Testing

### Automatic testing

Python code validated through [PEP8 validator](https://pep8ci.herokuapp.com/) - All clear, no errors found


## Manual testing

### User goals

| User goal | How are they achived | 
| --- | --- | 
| Think about goals and dreams | Design a fun and easy-to-use budget calculator that focuses on the fun part making a budget; thinking about goals and dreams. | 
| Learn how to achive those goals and dreams | Analyse the results and compare users budget against general guidelines and give helpful tips about spending and reducing costs. |
| Know how to use the application | Design a CLI tutorial that prepares the user for navigating and using the application. |
| Calculate budget and see how long it takes to reach a specific goal | Let the user set a specific goal and estimate a cost of that goal. Check users budget and see how much of the budget that can currently be used towards this goal. Calculate how long it will take to reach the goal and display this information to the user in a helpful way. | 
| Try different budgets or calculate for different goals | Design a fast re-use feature that helps the user change their budget or goal quickly instead of having to restart the entire program after every calculation. | 

### Features

| Feature tested | Expected outcome | Testing Performed | Result | Pass / fail | 
| --- | --- | --- | --- | --- |
| **Welcome screen** | 
| Display welcome screen | Show welcome message | Load page or click "RUN PROGRAM" button | Application is loaded and welcome message is displayed | Pass |
| Controlled speed | Generate different text in different speeds | Start application and watch | Different texts are generated at different speeds | Pass |
| **CLI tutorial** |
| Enter tutorial | Start the tutorial | Enter the option "1" into terminal and press ENTER | Tutorial starts | Pass |
| Tutorial step 1 | Continue tutorial | Press ENTER as instructed | Tutorial continues | Pass |
| Tutorial step 2 | Continue tutorial | Enter the required text "hello" and "Hello" into the terminal | Tutorial continues to the next lesson | Pass |
| Tutorial step 3 | Continue tutorial | Press enter a few times quickly, then enter "OK" as instructed | Tutorial continues and explains the previous lesson | Pass |
| Tutorial step 4 | End application | Read information and then press "Ctrl-C" | Message is displayed saying that Ctrl-C was pressed and then application stops running | Pass |
| **Dreams and goals** |
| Goals | Be able to enter goal | Write a goal when prompted and press ENTER | Application confirms input was valid by printing it to the terminal and proceeding to the next screen | Pass |
| **Budget calculator** |
| Enter data | Be able to enter data in the calculator | Write data into calculator  when prompted and press ENTER | Application confirms input was valid by printing it to the terminal and proceeding to the next category | Pass |
| **Number input validation** |
| Empty field | Display error message | Press ENTER without writing a number in the terminal | Custom error message is displayed and data have to be entered again | Pass |
| Number is not entered | Display error message | Enter a letter or symbol and press ENTER | Custom error message is displayed and data have to be entered again | Pass |
| Negative value | Display error message | Attempt to enter the negative value " -5 " and press ENTER | Custom error message is displayed and data have to be entered again | Pass |
| Too many characters | Display error message | Enter more than 20 characters | Custom error message is displayed and data have to be entered again | Pass |
| **Text input validation** |
| Empty field | Display error message | Press ENTER without writing anything into the terminal first | Custom error message is displayed and data have to be entered again | Pass |
| Too many characters | Display error message | Enter more than 60 characters | Custom error message is displayed and data have to be entered again | Pass |
| **Specific question validation** |
| Enter valid data | Continue application | Enter one of the given valid options to the question | Input is accepted and application proceed according to the users choice | Pass |
| Enter invalid data | Display error message | Enter something other then the valid responses | Custom error message is displayed and question is asked again | Pass |
| **Error handling** |
| ZeroDivisionError Goal | Not able to get error | Enter the number 0 as income into the budget calculator | Message displayed on result screen that goal can not be reached | Pass |
| ZeroDivisionError Analysis | Not able to get error | Enter the number 0 as income into the budget calculator | Message displayed on analysis screen that comparason can not be calculated since income is 0. | Pass |
| **Fast re-use** |
| Change goal | Only change goal | Choose nr 1 to change goal | Goal screen is display and new goal has to be entered, then calculation is run again | Pass |
| Change budget | Only change budget | Choose nr 2 to change budget | Data input for budget is displayed and new data has to be entered, then calculation is run again | Pass |
| Change goal & budget | Change both goal and budget | Choose nr 3 to change goal and budget | Goal screen is display and new goal has to be entered, then data input for budget is displayed and new data has to be entered, then calculation is run again | Pass |
| Continue | Continue with cost analysis | Choose nr 4 to continue | Message is displayed and cost analysis begins | Pass |
| **Other features** |
| Financial analysis | Show analysis with entered budget | Enter data in budget calculator and choose to continue with cost analysis | Cost analysis based on budget input is displayed and compared with general guidelines | Pass |
| Bonus tip: Yes | Able to choose to see a bonus tip | Write "Yes" and press enter when prompted | Bonus tip is displayed | Pass |
| Bonus tip: Yes | Able to skip bonus tip | Write "No" and press enter when prompted | Bonus tip is not displayed | Pass |
| Start over: Yes | Able to start over with new calculation | Write "Yes" and press enter when prompted | Calculator is restarted and new goal and budget needs to be entered | Pass |
| Start over: No | Able to choose to end application instead of starting over | Write "No" and press enter when prompted | A final message is displayed and application ends | Pass |


### Browser
Website has been tested on Google Chrome, Microsoft Edge, Firefox, and Samsung Internet Browser.

| Feature tested \  On browser | Google Chrome | Microsoft Edge | Firefox | Samsung Internet  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| **Other features** |
|  |  |  |  |  |



## Bugs

### Solved bugs

A large number of bugs was accidentally created during development and had to be fixed.
Fixes included:
- looking through code line by line
- using print() statements to see what was acctually going on
- review commit history
- search google for possible solutions
- a lot of trial and error


### Unfixed bugs

- None