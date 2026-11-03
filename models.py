from sqlalchemy import Column, Integer, String

from database import Base


# Book is a Python class mapped to the books table in SQLite.
class Book(Base):
    # This is the table name that will be created in SQLite.
    __tablename__ = "books"

    # id is the primary key. SQLite will generate it automatically.
    id = Column(Integer, primary_key=True, index=True)

    # nullable=False means these columns are required.
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)