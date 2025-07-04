from enum import StrEnum

import requests
from bs4 import BeautifulSoup, ResultSet, PageElement
from pydantic import BaseModel


class Tags(StrEnum):
    WEEKEND = 'container-weekend'
    MORE = 'container-more-features'
    SPORT = 'container-sport'


class News(BaseModel):
    container: Tags

    def __get_news_data(self):
        with requests.get('https://www.theguardian.com/uk') as response:
            soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def fetch_articles(self):
        soup = self.__get_news_data()
        container = soup.find(id=self.container)
        uls: BeautifulSoup | ResultSet | PageElement = container.find_all('ul')
        for ul in uls:
            for li in ul:
                try:
                    category: str = li.find(class_='card-headline').find('div').text
                    title: str = li.find_all('div')[1].find('a')['aria-label']
                    yield dict(title=title, featured_text=category)
                except Exception:
                    pass
