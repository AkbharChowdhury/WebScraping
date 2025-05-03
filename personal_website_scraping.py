import requests
from bs4 import BeautifulSoup


def tag_is_not_empty(tag: int):
    return tag not in [-1, None]


def main():
    show_project_details()
    # single_project_details()


def get_project_tags():
    return [
        {'tag': 'h3'},
        {'tag': 'p'},
        {'tag': 'ul'},
        {'tag': 'script'},
    ]


def show_project_details():
    with requests.get('https://akbharchowdhury.github.io/portfolio_generator/') as response:
        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
        projects = soup.find(id="projects")

    tags = get_project_tags()

    for project in projects:
        for tag in tags:
            html_tag = tag.get('tag')
            project_tag = project.find(html_tag)
            if tag_is_not_empty(project_tag):
                if html_tag == 'ul':
                    all_features = [feature.text.strip() for index, feature in enumerate(project_tag, start=1)  if feature not in ['\n']]
                    for i, feature in enumerate(all_features, start=1):
                        print(f'{i}) {feature}')
                else:
                    content = project_tag.text.strip()
                    print(content)

            if html_tag == 'script':
                if tag_is_not_empty(project_tag):
                    script = project.find(html_tag)
                    print('link to colab:'.title(), script['src'])
        print()


def single_project_details():
    with requests.get('https://akbharchowdhury.github.io/portfolio_generator/') as response:
        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
        projects = soup.find(id="projects")
    heading = projects.h3.text
    description = projects.p.text
    projects_features = projects.ul
    print(heading)
    print(description)
    for index, feature in enumerate(projects_features, start=1):
        print(f'- {feature.text}'.strip())


if __name__ == '__main__':
    main()
