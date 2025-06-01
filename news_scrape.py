import requests
from bs4 import BeautifulSoup
import json


def get_news_data():
    with requests.get('https://www.theguardian.com/uk') as response:
        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
    return soup


def fetch_articles(container_div_id: str = 'container-more-features'):
    soup = get_news_data()
    container = soup.find(id=container_div_id)
    uls = container.find_all('ul')
    for ul in uls:
        for li in ul:
            div_container = li.find('div').find('div')
            category: str = li.find(class_='card-headline').find('div').text
            title: str = div_container.find('a')['aria-label']
            yield dict(title=title, featured_text=category)


def main():
    cats = {
        'weekend': 'container-weekend',
        'more': 'container-more-features',
        'sport': 'container-sport'
    }

    news = list(fetch_articles(cats.get('more')))
    print(json.dumps(news, indent=4))


if __name__ == '__main__':
    main()
