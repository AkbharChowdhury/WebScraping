import requests
from bs4 import BeautifulSoup


def tag_is_not_empty(tag: int):
    return tag not in (-1, None, '\n')


def main():
    print('A list of my personal projects:')
    show_project_details()
    print('My first project details')
    single_project_details()


def show_project_features(project_tag: BeautifulSoup | int):
    all_features: set[str] = {feature.text.strip() for feature in project_tag if tag_is_not_empty(feature)}
    for i, feature in enumerate(all_features, start=1):
        print(f'{i}) {feature}')


def get_project_data():
    with requests.get('https://akbharchowdhury.github.io/portfolio_generator/') as response:
        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
        return soup.find(id="projects")


def show_colab_link(tag: str, project_tag: BeautifulSoup | int):
    if 'script'.casefold() == tag.casefold() and tag_is_not_empty(project_tag):
        link = 'https://colab.research.google.com/gist/AkbharChowdhury/8b22b62988589e939d563fcbb6e9d0a3/data_visualisation.ipynb'
        print('Link to Colab:'.title(), link)

def show_project_details():
    tags: list[str] = ['h3', 'p', 'ul', 'script']
    projects = get_project_data()

    for project in projects:
        for tag in tags:
            project_tag = project.find(tag)
            if tag_is_not_empty(project_tag):
                if not tag == 'ul':
                    print(project_tag.text.strip())
                    continue
                show_project_features(project_tag)
            show_colab_link(tag=tag, project_tag=project_tag)


def single_project_details():
    projects: BeautifulSoup = get_project_data()
    heading = projects.h3.text
    description = projects.p.text
    projects_features = projects.ul
    print(heading)
    print(description)
    for index, feature in enumerate(projects_features, start=1):
        print(f'- {feature.text}'.strip())


if __name__ == '__main__':
    main()
