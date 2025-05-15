from projects import Project


def main():
    project = Project()
    print('A list of my personal projects:')
    project.show_project_details()
    print('My first project details')
    project.single_project_details()


if __name__ == '__main__':
    main()
