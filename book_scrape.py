import requests
from bs4 import BeautifulSoup
import json
from books_handler import BookHandler


def fetch_book_request(page_number: int):
    with requests.get(f'https://books.toscrape.com/catalogue/page-{page_number}.html') as response:
        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
    return soup


def fetch_book(page_number: int):
    soup = fetch_book_request(page_number)
    book_elements = soup.find_all('article', class_='product_pod')
    book_data = BookHandler.fetch_book_data(book_elements)
    books = (book for book in book_data)
    return books


def main():
    all_books: list[dict[str, str]] = []
    max_pages: int = 10
    for current_page in range(1, max_pages + 1):
        books_on_page = list(fetch_book(current_page))
        all_books.extend(books_on_page)
        print(f'Books on page {current_page}: {books_on_page}')
    with open('books.json', 'w') as f:
        json.dump(all_books, f, indent=2)
    print('data is saved to books.json')


if __name__ == '__main__':
    main()
