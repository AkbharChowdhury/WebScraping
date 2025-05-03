import requests
from bs4 import BeautifulSoup


def main():
    with requests.get('https://example.com') as response:
        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
        # print(soup.prettify())
        title: str = soup.title.text
        content = soup.find('p').text
        links = [a['href'] for a in soup.find_all('a')]
        print(f'{title=}')
        print(f'{content=}')
        print(f'{links=}')


if __name__ == '__main__':
    main()
