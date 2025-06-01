from bs4 import ResultSet, PageElement, Tag, NavigableString

book_catalogue_url: str = 'https://books.toscrape.com/catalogue/'


class BookHandler:
    @staticmethod
    def fetch_book_data(book_elements: ResultSet[PageElement | Tag | NavigableString]):
        for book in book_elements:
            title = book.find('h3').find('a')['title']
            price = book.find('p', class_='price_color').text
            stock = 'In stock' if 'In stock' in book.find('p', class_='instock availability').text else 'Out of stock'
            rating = book.find('p', class_='star-rating')['class'][1]
            link = book.find('h3').find('a')['href']
            yield {
                'title': title,
                'price': price,
                'stock': stock,
                'rating': rating,
                'link': f'{book_catalogue_url}{link}'
            }
