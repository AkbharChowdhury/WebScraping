import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, date
def is_weekend(d = datetime.today()):
  return d.weekday() > 4

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
            try:
                category: str = li.find(class_='card-headline').find('div').text
                title: str = li.find_all('div')[1].find('a')['aria-label']
                yield dict(title=title, featured_text=category)
            except Exception:
                pass

def show_article_details(title: str):
    news = list(fetch_articles(title))
    print(json.dumps(news, indent=4))

def main():
    cats = {
        'weekend': 'container-weekend',
        'more': 'container-more-features',
        'sport': 'container-sport'
    }
    show_article_details('container-sport')
    if is_weekend():
        show_article_details(cats.get('more'))



if __name__ == '__main__':
    main()
