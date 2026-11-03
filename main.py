from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db

# Create the database tables when the app starts.
# This creates the 'books' table defined in models.py if it doesn't exist.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Books API is running"}


@app.get("/books", response_model=List[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    # Depends(get_db) provides an independent database session for this request.
    books = db.query(models.Book).all()
    return books


@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    # Find one book by its primary key.
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Book not found"
        )

    return book


@app.post("/books", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book_data: schemas.BookCreate, db: Session = Depends(get_db)):
    # Create a new Book instance using validated data from Pydantic
    book = models.Book(
        title=book_data.title,
        author=book_data.author,
        year=book_data.year
    )

    # Add to session, commit to save, and refresh to retrieve generated ID
    db.add(book)
    db.commit()
    db.refresh(book)

    return book