# TextIndexer

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
