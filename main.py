import uvicorn 
from fastapi import FastAPI 
from starlette.requests import Request 
from starlette.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import Dict, List


app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Book(BaseModel):
    Title: str = Field(min_length=1, description="БЛА-БЛА")
    Author: str = Field(min_length=3, max_length=30, description="БЛА-БЛА")
    Pages: int = Field(gt = 10, description="БЛА-БЛА")

library: Dict[str, List[Book]] = {}

@app.post("/books/")
def create_Book(book: Book):
    if book.Author not in library:
        library[book.Author] = []
    library[book.author].append(book)
    return {"message": "Книжка додана і т.д"}

@app.get("/books/{author}")

def get_books_by_author(author: str):
    if book.Author not in library:
        raise HTTPException(status_code= 404, detail= "Автора не найшло")
    return library[author]

@app.put("/books/{author}/{title}")
def update_book(author: str, title: str, new_pages: int):
    if author not in library or not any(book.title == title for book in library[author]):
        raise HTTPException(status_code=404, detail="Книжку не найшло шось")
    for book in library[author]:
        if book.title == title:
            book.pages = new_pages
            return {"message": "Книжка оновлена успішно"}
        
@app.delete("/books/{author}/{title}")
def delete_book(author: str, title: str):
    if author not in library or not any(book.title == title for book in library[author]):
        raise HTTPException(status_code= 404, detail= "Книжку не знайшло")
    library[author] = [book for book in library[author] if book.title != title]
    return {"message": "Книжка видалена успішно"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)