# Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.


import requests
import json


class git_repo():
    def __init__(self, git_link):
        self.git_link = git_link
    def get_open_repos(self, filename):
        self.filename =filename
        response = requests.get(self.git_link)
        for repo in response.json():
            if repo['private'] == False:
                with open(self.filename, 'a', encoding='utf-8') as file:
                    json.dump(repo, file)
            else:
                pass

try_class = git_repo(git_link=input('Вставить ссылку: '))
try_class.get_open_repos('repos.json')