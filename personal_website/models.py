import requests
from bs4 import BeautifulSoup

from typography import bold_text

tag_is_not_empty = lambda tag: tag not in (-1, None, '\n')


class Project:

    def __show_project_features(self, project_tag: BeautifulSoup | int):
        all_features: set[str] = {feature.text.strip() for feature in project_tag if tag_is_not_empty(feature)}
        for number, feature in enumerate(all_features, start=1):
            print(f'{number}) {feature}')

    def __get_project_data(self):
        with requests.get('https://akbharchowdhury.github.io/portfolio_generator/') as response:
            soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
            return soup.find(id="projects")

    def __show_colab_link(self, tag: str, project_tag: BeautifulSoup | int):
        if 'script'.casefold() == tag.casefold() and tag_is_not_empty(project_tag):
            link = 'https://colab.research.google.com/gist/AkbharChowdhury/8b22b62988589e939d563fcbb6e9d0a3/data_visualisation.ipynb'
            print('Link to Colab:'.title(), link)

    def show_project_details(self):
        tags: set[str] = {'h3', 'p', 'ul', 'script'}
        projects = self.__get_project_data()
        for project in projects:
            for tag in tags:
                project_tag = project.find(tag)
                if tag_is_not_empty(project_tag):
                    if not tag == 'ul':
                        print(bold_text(project_tag.text.strip()))
                        continue
                    self.__show_project_features(project_tag)
                self.__show_colab_link(tag=tag, project_tag=project_tag)

    def single_project_details(self):
        projects: BeautifulSoup = self.__get_project_data()
        heading = projects.h3.text
        description = projects.p.text
        projects_features = projects.ul
        print(bold_text(heading))
        print(description)
        for index, feature in enumerate(projects_features, start=1):
            print(f'- {feature.text}'.strip())
