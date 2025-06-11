import json
from datetime import datetime
from news_model import News, Tags


def is_weekend(d: datetime = datetime.today()):
    return d.weekday() > 4


def main():
    tag: str = Tags.WEEKEND.name if is_weekend() else Tags.SPORT.name
    news = News(__container=tag)
    print(json.dumps(list(news.fetch_articles()), indent=4))


if __name__ == '__main__':
    main()
