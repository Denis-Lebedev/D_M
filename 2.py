# Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

import requests
import json

url = 'https://api.vk.com/method/groups.get?'
headers = {
    'User Agent	': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
user_id = input('ID вконтакте')
token = input('Токен доступа')

params = {'user_id': user_id, 'access_token': token, 'extended': 1, 'v': '5.130'}

response = requests.get(url, headers=headers, params=params)
group_list = []
groups = response.json()['response']
for group in groups['items']:
    if group['is_closed'] == 0:
        group_list.append(group)
    else:
        pass

with open('user_data.txt', 'w', encoding='utf-8')as file:
    file.write(str(group_list))

