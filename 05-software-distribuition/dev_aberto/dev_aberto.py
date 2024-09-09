import requests


def hello():
    username = input('Digite seu usuário: ')
    c = requests.get('https://api.github.com/repos/insper/dev-aberto/commits')
    info = c.json()
    commit_info = info[0]['commit']['author']
    return commit_info['date'], commit_info['name']