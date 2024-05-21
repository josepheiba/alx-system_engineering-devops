#!/usr/bin/python3
"""
this code will get data from api and process it
"""
import json
import requests


if __name__ == '__main__':
    """
    main function
    """
    api_url_users = 'https://jsonplaceholder.typicode.com/users'
    api_url_todos = 'https://jsonplaceholder.typicode.com/todos'

    result_users = requests.get(api_url_users)
    result_todos = requests.get(api_url_todos)

    result_users = json.loads(result_users.text)
    result_todos = json.loads(result_todos.text)

    user_id_list_dicts = {}
    for user in result_users:

        user_todos = []
        for todo in result_todos:
            if todo['userId'] == user['id']:
                todo_temp = todo.copy()
                todo_temp.pop('id')
                todo_temp.pop('userId')
                todo_temp.update({'username': user['username']})
                todo_temp.update({'task': todo['title']})
                todo_temp.pop('title')
                new_order = ['username', 'task', 'completed']
                todo_temp = {key: todo_temp[key] for key in new_order}
                user_todos.append(todo_temp)
        user_id_list_dicts[user['id']] = user_todos

    with open("todo_all_employees.json", 'w') as file:
        json.dump(user_id_list_dicts, file)
