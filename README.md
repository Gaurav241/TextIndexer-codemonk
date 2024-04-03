# TextIndexer

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [API Endpoints](#api-endpoints)
5. [Installation Guide](#installation-guide)
    - [Clone the Repository](#1-clone-the-repository)
    - [Configure the Database](#2-configure-the-database)
    - [Install Dependencies](#3-install-dependencies)
    - [Database Migrations](#4-database-migrations)
    - [Running the Server](#5-running-the-server)
    - [Accessing the Application](#6-accessing-the-application)
6. [Usage Instructions](#usage-instructions)
    - [Users](#users)
    - [Paragraphs](#paragraphs)
    - [Search](#search)
7. [Contributing](#contributing)

## Introduction
This project provides a REST API that allows users to input multiple paragraphs of text, which are then stored in a PostgreSQL database with mappings of words to paragraphs. Users can search for a word, and the API will list the top 10 paragraphs where the word appears. This project is built using Django Rest Framework and is designed with extensibility and best coding practices in mind.

## Features
- User authentication and session management.
- RESTful endpoints for inputting text and searching for words within stored paragraphs.
- PostgreSQL for efficient data storage and retrieval.
- Swagger integration for API documentation and testing.

## Tech Stack
- Django Rest Framework
- PostgreSQL

## API Endpoints
- `/admin/`: Provides access to the Django admin interface.
- `/swagger/`: Provides access to Swagger UI for interactive API documentation.
- `/redoc/`: Provides access to ReDoc for an alternative API documentation view.
- `/users/`: Custom API endpoint for listing and creating users.
- `/paragraphs/`: Custom API endpoint for listing and creating paragraphs.
- `/search/`: Custom API endpoint for searching words in paragraphs.

## Installation Guide

Follow these steps to set up the TextIndexer project on your local machine.

### 1) Clone the Repository

- Start by cloning the TextIndexer repository from GitHub to your local machine:

```
git clone https://github.com/Gaurav241/TextIndexer.git
```

- Navigate into the cloned repository:
```
cd TextIndexer
```

### 2) Configure the Database

Before running the application, you need to configure the PostgreSQL database in TextIndexer/settings.py. Open this file in your preferred text editor and locate the DATABASES configuration. It should look something like this:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Replace your_db_name, your_db_user, and your_db_password with your actual PostgreSQL database name, user, and password. If your database is hosted on a different server or port, update the HOST and PORT accordingly.

### 3) Install Dependencies

Install the project dependencies by running the following command in your terminal:
```
pip install -r requirements.txt
```
### 4) Database Migrations

With your database configured and dependencies installed, the next step is to apply the database migrations. Run the following commands in your terminal:
```
python manage.py migrate
```
This command sets up your database schema according to the models defined in the project.

### 5) Running the Server

To start the Django development server, execute:
```
python manage.py runserver
```
### 6) Accessing the Application

Once the server is running, you can navigate to the Swagger documentation to interact with the API:
```
http://127.0.0.1:8000/swagger/
```
Here, you will find a UI to test the various API endpoints, such as creating users, inputting paragraphs, and searching for words within those paragraphs.


## Usage Instructions

### Step-by-Step Guide

#### Users
1. **Create User (POST)**
   - Navigate to `/users/` and click on "Try it out"
   - Input the user details as JSON:
     ```
     {
       "name": "your_name",
       "email": "email@email.com",
       "dob": "2000-04-03"
     }
     ```
   - Click "Execute" to create the user.

2. **List Users (GET)**
   - Navigate to `/users/` and click on "Try it out", then "Execute".
   - The output will list all users, for example:
     ```
     [
       {
         "id": 1,
         "name": "your_name",
         "email": "email@email.com",
         "dob": "2000-04-03",
         "created_at": "2024-04-03T16:29:58.919120Z",
         "updated_at": "2024-04-03T16:29:58.919120Z"
       }
     ]
     ```
### Paragraphs

3. **Create Paragraph (POST)**
   - Navigate to `/paragraphs/` and click on "Try it out".
   - In the request body section, input the paragraph details as JSON:
     ```
     {
       "content": "Example Paragraph"
     }
     ```
   - Click "Execute" to submit the paragraph.
   - Upon success, the response will include the paragraph's ID and content:
     ```
     {
       "id": 1,
       "content": "Example Paragraph"
     }
     ```

4. **List Paragraphs (GET)**
   - Navigate to `/paragraphs/` and click on "Try it out", then "Execute".
   - The output will list all paragraphs stored in the database, including their IDs and content.

### Search

5. **Search for a Word (GET)**
   - Navigate to `/search/` and click on "Try it out".
   - In the `word` parameter field, enter the word you want to search for within the paragraphs. For example:
     ```
     word: example
     ```
   - Click "Execute" to perform the search.
   - The response will list paragraphs where the word appears, showing up to the top 10 matches. Each match includes the paragraph's ID and content. Example response for a search:
     ```
     [
       {
         "id": 2,
         "content": "Example Paragraph"
       }
     ]
     ```

## Contributing
- Contributions are welcome! Please feel free to submit pull requests or open issues to discuss proposed changes or improvements.
