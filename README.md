<div align="center">

  <h1>Hexlet project: Task Manager</h1>

  [A simple web application for managing team tasks](https://python-project-52-glfi.onrender.com/)







### Hexlet tests and linter status:
[![Actions Status](https://github.com/Asgef/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Asgef/python-project-52/actions)
[![linter-tests](https://github.com/Asgef/python-project-52/actions/workflows/main.yml/badge.svg)](https://github.com/Asgef/python-project-52/actions/workflows/main.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/2ef56828174fc5ff604d/maintainability)](https://codeclimate.com/github/Asgef/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2ef56828174fc5ff604d/test_coverage)](https://codeclimate.com/github/Asgef/python-project-52/test_coverage)

</div>

## Description

This project was created as part of the "Python Developer" course on the [Hexlet educational platform](https://hexlet.io).


**Task manager** is a small web application based on the Python framework Django, designed for managing tasks in a small team.

This project applies the fundamental principles of modern web development based on the MVC architecture, including routing, request handling, template creation, and database interaction using the built-in ORM.

Django's built-in ORM allows for consistent interaction with the project's databases, PostgreSQL and SQLite.

Bootstrap is used together with the built-in DjangoTemplates engine to create the appearance of the web application.

## Features

- Create tasks;
- Assign executors;
- Set task status and assign labels;
- Filter tasks by one or more criteria;
- User authentication and registration.

## Usage

1. Register in the application:
   - Use your first name, last name, and username.
   - Create a strong password.
2. Log in:
   - Use your username and password.
3. "Users" tab:
   - View team members.
   - Edit your own information.
4. "Statuses" tab:
   - View the list of statuses.
   - View and edit statuses.
5. "Labels" tab:
   - View the list of labels.
   - View and edit labels.
6. "Tasks" tab:
   - View the list of tasks.
   - Filter the list of tasks by one or more criteria.
   - Get detailed information about each task.
   - Edit tasks.
   - Create tasks, assign executors, and set status and labels.



## Bult With

- Python
- Django
- PostgreSQL
- Bootstrap 5
- Rollbar
- Whitenoise

## Demonstration
Check out the demo version deployed on Render:
https://python-project-52-glfi.onrender.com/


## Installation

 ### Requirements
Before starting the installation, make sure you have the following components 
 installed:

- Python (version 3.11 or higher)
- PIP (version 24.0 or higher)
- Poetry (Python package installer)
- Git (version 2.43 or higher)
- PostgreSQL (version 16.2 or higher), optional.


### Steps

#### 1. Cloning the repository.
Execute the following command in your terminal to clone the repository to your local machine:


    git clone git@github.com:Asgef/python-project-52.git


#### 2. Installing Dependencies.
Navigate to the project directory and execute the command to install dependencies:


    make install


#### 3. Setting up environment variables.
Create a .env file in the root directory of the project and specify the necessary environment variables, for example:


    SECRET_KEY = '{your secret key}'
    
    # optional
    DATABASE_URL = postgresql://{provider}://{user}:{password}@{host}:{port}/{db}
    POST_SERVER_ITEM_ACCESS_TOKEN='{your secret key}'


#### 4. Build the project
Perform migrations and create a directory for static files:


    make build


#### 5. Running the application.
Launch the web application using the following command:

    make start


#### 6. Running the application.
Verification:
Open a web browser and navigate to http://localhost:8000 to verify that the application has been successfully installed and is running.


#### 7. Using the Database

This project is configured to use SQLite in the development environment and PostgreSQL in the production environment. If you need to use PostgreSQL during development, set the DATABASE_URL variable in your .env file and update the entry in settings.py:

```
    DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}
```

#### 8. Using Rollbar
You can use the [error monitoring service](https://rollbar.com).
1. Set the POST_SERVER_ITEM_ACCESS_TOKEN variable in your .env file. The token will be provided to you during registration.
2. In settings.py, set the variable:

   ```
   
   ROLLBAR = {
       'access_token': os.getenv('POST_SERVER_ITEM_ACCESS_TOKEN'),
       'environment': 'development' if DEBUG else 'production',
       'branch': 'main',
       'root': 'BASE_DIR',
   }
   
   ```

3. Navigate to the project directory, and in the terminal, run the command poetry shell.

4. Start the Python REPL and execute the following commands:

   ```
   from dotenv import load_dotenv
   
   load_dotenv()
   
   
   rollbar.init(
           access_token='your_access_token',
           environment='testenv',
           code_version='1.0'
       )
   
   ```


