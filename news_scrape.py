import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from pydantic import BaseModel
from enum import StrEnum


class Tags(StrEnum):
    WEEKEND = 'container-weekend'
    MORE = 'container-more-features'
    SPORT = 'container-sport'


def is_weekend(d=datetime.today()):
    return d.weekday() > 4


class News(BaseModel):
    __container: str = 'container-more-features'

    def __get_news_data(self):
        with requests.get('https://www.theguardian.com/uk') as response:
            soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def fetch_articles(self):
        soup = self.__get_news_data()
        container = soup.find(id=self.__container)
        uls = container.find_all('ul')
        for ul in uls:
            for li in ul:
                try:
                    category: str = li.find(class_='card-headline').find('div').text
                    title: str = li.find_all('div')[1].find('a')['aria-label']
                    yield dict(title=title, featured_text=category)
                except Exception:
                    pass


def main():
    tag: str = Tags.WEEKEND.name if is_weekend() else Tags.SPORT.name
    news = News(__container=tag)
    print(json.dumps(list(news.fetch_articles()), indent=4))


if __name__ == '__main__':
    # print(Tags('MORE'))

    main()
