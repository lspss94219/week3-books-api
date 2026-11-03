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
   
