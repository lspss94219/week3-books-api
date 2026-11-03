# Week 3: Books API

A simple REST API for managing books built with FastAPI, SQLAlchemy, and SQLite.

## Requirements & Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\Activate.ps1  # Windows
   ```
2. Install Requirements
   ```
   pip install -r requirements.txt
   ```

4. Running the App
   Start the Uvicorn server
   ```
   uvicorn main:app --reload
   ```
   Access the interactive API docs
   ```
   http://127.0.0.1:8000/docs
   ```
   
# API Endpoints
   POST /books - add a new book
   GET / - Health check message
   GET /books - Retrieve all books
   GET /books/{book_id} - retrieve a single book by id

# Testing Results
   1. POST /books(Valid Data)
      
      Status 201
      ```
      {
      "title": "Clean Code",
      "author": "Robert Martin",
      "year": 2008,
      "id": 2
      }

   2. POST /books(Validation Failure)
      
      Status 422
      ```
      {
      "detail": [
      {
      "type": "string_too_short",
      "loc": ["body", "title"],
      "msg": "String should have at least 2 characters",
      "input": "A",
      "ctx": { "min_length": 2 }
      },
      {
      "type": "string_too_short",
      "loc": ["body", "author"],
      "msg": "String should have at least 2 characters",
      "input": "B",
      "ctx": { "min_length": 2 }
      },
      {
      "type": "greater_than_equal",
      "loc": ["body", "year"],
      "msg": "Input should be greater than or equal to 1900",
      "input": 1800,
      "ctx": { "ge": 1900 }
      }
      ]
      }
   3. GET /books
      
      Status 200
      ```
      [
      {
      "title": "Clean Code",
      "author": "Robert Martin",
      "year": 2008,
      "id": 1
      },
      {
      "title": "Clean Code",
      "author": "Robert Martin",
      "year": 2008,
      "id": 2
      }
      ]
    
   4. GET /books/1
      
      Status 200
      ```
      {
      "title": "Clean Code",
      "author": "Robert Martin",
      "year": 2008,
      "id": 1
      }

   5. GET /books/999
      
      Status 404 Not Found
      ```
      {
      "detail": "Book not found"
      }
