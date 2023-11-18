# Dream Achiever

![Amiresponsive image](https://res.cloudinary.com/dmntcacug/image/upload/v1700167217/Amiresponsive_nl4tfn.png)


Link to live website: [Dream Achiever](https://dream-achiever-3a6af54c4f68.herokuapp.com/) <br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)

<hr>

## Table of contents

TODO: Update table of content

* [User Experience (UX)](#user-experience-ux)
    * [User stories](#user-stories)
        * [Website goals](#website-goals)
        * [User goals](#user-goals)
* [Design](#design)
    * [Wireframes](#wireframes)
    * [Flowchart](#flowchart)
* [Features](#features)
    * [Welcome screen](#welcome-screen)
    * [Controlled speed](#controlled-speed)
    * [CLI tutorial](#cli-tutorial)
    * [Dreams and goals](#dreams-and-goals)
    * [Budget calculator](#budget-calculator)    
    * [Input validation and error handling](#input-validation-and-error-handling)
    * [Fast re-use](#fast-re-use)
    * [Financial analysis](#financial-analysis)
* [Future features](#future-features)
* [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Frameworks & Tools](#frameworks--tools)
* [Data model](#data-model)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Heroku](#deployment-to-heroku)
    * [Changes](#changes-to-the-code)
    * [Local development](#local-development)
        * [Forking](#forking-the-project)
        * [Cloning](#cloning-the-project)
* [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Code](#code)

<hr>

## User Experience (UX)

This website is a financial tool made to help people reach their goals and achieve their dreams. It does so by providing a simple budget calculator that is very easy to use. The user enters data about income and expenses into easy user-friendly categories and then the program calculates how long it will take to reach their goal. 

It helps people to think about budget as something fun instead of boring or restricting. It is about prioritizing what is the most important and make a realistic plan to achieve it.

After the calculator is done and results are presented, helpful tips are shown on how to cut costs and some insights on how to think about each category. It also compares the users budget to the general guidelines from the Credit Counselling Society. The user also has an option to learn about another easy to use budgeting tool before leaving.


### User stories

#### Website goals
- Help people clarify their goals and think about ways to achive them
- Provide a useful tool that is easy to use.
- Give users financial advice to help reach their goal

#### User goals
- Think about goals and dreams
- Learn how to achive those goals and dreams
- Know how to use the application
- Calculate budget and see how long it takes to reach a specific goal
- Try different budgets or calculate for different goals


## Design
#### Wireframes
<details><summary>Screenshot of the initial wireframes</summary> <p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1699387577/PP3_Wireframe_dxzz7q.png" alt="Picture of the wireframes" width="600"/></p> </details>

#### Flowchart

Shows the first sketch of the basic logic used by the application and project goals. It show the users path through the application. More complicated features were added later to give user more options on how to navigate.

<p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1699359420/Flowchart_-_PP3_hyhjx7.png" alt="Flowchart image" width="800"/></p>

## Features

### Welcome screen

The welcome screen is the first thing the user sees when entering the website. The Pyfiglet font Big Money sets the right tone and the words "Dream Achiever" together with the background image puts the user in a positive frame of mind right away.

<details><summary>Screenshot of the feature</summary> <p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1700232792/feature-welcome_iwggf4.jpg" alt="Picture of the welcome screen" width="700"/></p> </details>


### Controlled speed

A combination of fast and slow text generation is used to create a pleasant user experience.

<details><summary>Screenshot of the slow writing feature</summary> <p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1700234544/feature-controlled-speed_ovvuin.jpg" alt="Picture of the slow writing feature" width="600"/></p> </details>


### CLI tutorial

Not everyone is familiar with CLI terminal interface, therefor a tutorial was added so that the user can learn how to use the application as well as some general do's and dont's. Also helpful information about budgeting and how to use the calculator is given to the user at appropriate times throughout the application.

<details><summary>Screenshot of the feature</summary> <p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1700233258/feature-cli-tutorial_vqzfza.jpg" alt="Picture of option for CLI tutorial" width="600"/></p> </details>

### Dreams and goals

Starting this budget calculator with thinking about dreams and fun life goals is the best way to make something as boring as a budget calculator into a positive and uplifting user experience.

<details><summary>Screenshot of the dream screen</summary> <p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1700233860/feature-dream_rn0jd8.jpg" alt="Picture of dream screen" width="600"/></p> </details>
<details><summary>Screenshot of the goal screen</summary> <p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1700234996/feature-goal_nw1bac.jpg" alt="Picture of the goal screen" width="600"/></p> </details>

### Budget calculator

The user is prompted to enter a specific goal and their financial data into various categories. The program then uses this data to make calculations about how long it will take the user to reach the goal.

<details><summary>Screenshot of the results screen</summary> <p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1700236022/feature-results_rmpym1.jpg" alt="Picture of the results screen" width="600"/></p> </details>


### Input validation and error handling

To prevent errors, each input is validated through different critera. Program will only accept the valid form of input to prevent various errors that might occur and cause the program to fail.

Program will also preemtivly check for ZeroDivisionError and adjust calculation and text output accordingly.

<details><summary>Screenshot of an example of input validation</summary> <p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1700235534/feature-input-validation_bdkfex.jpg" alt="Picture of example of input validation" width="600"/></p> </details>

### Fast re-use

In order to make this a truly useful tool, the fast re-use feature was implemented. Right after the results the user can choose to try another calculation immediately. This makes the application much faster to use and re-use. This makes it a lot more user friendly.

<details><summary>Screenshot of the fast re-use feature</summary> <p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1700236020/feature-fast-reuse_a1jyjk.jpg" alt="Picture of the fast re-use feature" width="600"/></p> </details>

### Financial analysis

After the user has finished using the calculator, testing different budgets or calculated different goals they can choose to proceed with the financial analysis. Program will guide the user through all categories and give helpful insights for each one. And at the end, give the user the option for a special bonus tip.

<details><summary>Screenshot of the financial analysis</summary> <p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1700237262/feature-financial-analysis_umxm7n.jpg" alt="Picture of the financial analysis" width="600"/></p> </details>

<details><summary>Screenshot of the 50-30-20 rule</summary> <p align="left"><img src="https://res.cloudinary.com/dmntcacug/image/upload/v1700237262/feature-50-30-20_fjrxxp.jpg" alt="Picture of the 50-30-20 rule" width="600"/></p> </details>


## Future features
- Add option to select different currencies to be displayed
- Add option to select weekly or monthly income
- Add data into a spreadsheet and send a budget template with data in email to the user


## Technologies used

### Languages
- Python
- HTML
- CSS

### Frameworks & Tools

- Git
- GitHub
- Heroku
- Balsamiq
- Lucidchart
- VS Code
- w3schools
- Stack Overflow
- Pyfiglet
- Favicon.io

## Data model

Program uses a User class to store the users financial data and help run calculations.
<br>Class is populated with properties through iterating a lists of categories.

### Control structures
- **Sequential**
<br>The default flow control stucture of the application is sequential
- **Selection**
<br>Implementing different choices and complex if-elif-else statements changes the outcome of the application based on the users input.
- **Repetition**
<br>For and while loops are used to collect data For each category from user While validating the input.


## Testing

Testing made in separate file [TESTING.md](TESTING.md)

## Deployment

#### Deployment to Heroku

1. Log in (or sign up) to Heroku. ( https://www.heroku.com/ )
2. From the dashboard, create a "new app" and follow the instructions.
3. When created go to the settings tab.
    - Add a Config Var with PORT as the key and 8000 as value.
    - Add 2 buildpacks, python and nodejs (in that order).
4. Go to the deployment tab.
    - Select GitHub as deployment method.
    - Connect app to the correct repository.
5. Choose to deploy either manully or enable automatic deploys.


#### Changes to the code
If changes has been made in local development, the requirements.txt might need to be updated.
- It is done by entering the following command in the terminal: 'pip3 freeze > requirements.txt'
- Updated file must then be commited and pushed to GitHub.

### Local development

#### Forking the project

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [Dream Achiever](https://github.com/NiclO1337/pp3-dream-achiever).
3. Click the Fork button in the top right corner.

#### Cloning the project

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [Dream Achiever](https://github.com/NiclO1337/pp3-dream-achiever).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH, or GitHub CLI, and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
Type 'git clone' into the terminal and then paste the link you copied in step 3. 
5. Press enter.

<br>Link to live website: [Dream Achiever](https://dream-achiever-3a6af54c4f68.herokuapp.com/) <br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)


## Credits

### Content

- [Budgeting Guidelines](https://nomoredebts.org/budgeting/budgeting-guidelines) from Credit Counselling Society

- Budgeting Basics from UNFCU: [The 50-30-20 Rule](https://www.unfcu.org/guides/the-50-30-20-rule/)

- What is [CLI](https://www.w3schools.com/whatis/whatis_cli.asp)


### Media

Picture by Pixabay: [Background image](https://www.pexels.com/sv-se/foto/himmel-moln-molnig-vader-417045/)

Image by Clker-Free-Vector-Images: [Favicon](https://pixabay.com/vectors/cloud-day-dark-cludy-weather-37010/)

### Code

- Inspiration from my own previous portfolio projects.

- Code institute for providing the template with the deployment terminal.

- Pyfiglet [tutorial](https://www.youtube.com/watch?v=U1aUteSg2a4)

- Typewriter style [tutorial](https://www.youtube.com/watch?v=2h8e0tXHfk0)

- Signal handling [Ctrl-C](https://code-maven.com/catch-control-c-in-python)

- Clear screen guide by [Coding ninjas](https://www.codingninjas.com/studio/library/how-to-clear-a-screen-in-python)