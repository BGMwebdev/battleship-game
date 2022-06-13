## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

-------------------------------------------------------------
# Tools for borrow

## Introduction
<hr>
Welcome to the Tools for borrow - system. This program aims to make life easier and cheaper for residents of an appartment building. Through registration the residents are provided with a system that will give insight in, and allow them to, borrow eachothers tools. 
<hr>

## Table of Content
1. [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
    - [Scope](#scope)
    - [User Manual](#user-manual)
3. [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
    - [Data Models](#data-models)   
4. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
    - [Python Validation](#Python-validation)
    - [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
10. [Deployment](#deployment)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)
<hr>

1. ## Project Goals
    - The goal of this project is ultimately to create a more sustainable way of living.
    - This project will aim to create a more circular economy through the exchange of equipment / tools, within a set group of people.

    ### User Goals
    - Be able to register / log in to a safe enviroment.
    - Add tools to a list, for other residents to use.
    - Search for the tools that I need.

    ### Site Owner Goals
    - Create an application with clear purpose.
    - Create an application that is intuitive and easy to navigate.
    - Create an application that will support the users need for tools.
<hr>

2. ## User Experience
    ### Target Audience
    - The target audience is everyone who lives in an appartment building or small community and wants to have a cheaper more co-created way of living, through the sharing of equipment / tools. 

    ### User Stories
    #### Resident user
    1. As a first time user I want to have a clear idea of the purpose of the application. 
    2. As a first time user I want to be able to register for the application.
    3. As a user I want to be able to log in.
    4. As a user I want to be able to search for a tool.
    5. I want to be able to see where I can borrow the tool.
    6. As a user I want to get feedback if the tool is not available or present.
    7. As a user I want to be able to add a tool to a list for others to use.
    8. As a user I want nagivation to be clear and easy.
    #### Site owner
    9. As a site owner I want registration and log in to be easy for the user.
    10. As a site owner I want user names and other information to be saved to a Google Spreadsheet.
    11. As a site owner I want input to be validated where necessary.
    12. As a site owner I want the user to be able to add and find a tool.
    13. As a site owner I want the user to get feedback if a tool is not available or present. 



    ### Scope
    - 
    ### User Manual
    - 
<hr>