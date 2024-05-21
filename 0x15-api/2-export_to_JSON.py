#!/usr/bin/python3
"""
this code will get data from api and process it
"""
import json
import requests
import sys


if __name__ == '__main__':
    """
    main function
    """
    argc = len(sys.argv)
    user_id = sys.argv[1]

    api_url_users = 'https://jsonplaceholder.typicode.com/users'
    api_url_todos = 'https://jsonplaceholder.typicode.com/todos'

    result_users = requests.get(api_url_users + '/' + user_id)
    result_todos = requests.get(api_url_todos)

    result_users = json.loads(result_users.text)
    result_todos = json.loads(result_todos.text)

    user_todos = []
    for todo in result_todos:
        if todo['userId'] == int(user_id):
            todo.pop('id')
            todo.pop('userId')
            todo.update({'username': result_users['username']})
            todo.update({'task': todo['title']})
            todo.pop('title')
            new_order = ['task', 'completed', 'username']
            todo = {key: todo[key] for key in new_order}
            user_todos.append(todo)
    user_id_list_dicts = {result_users['id']: user_todos}

    with open(f"{result_users['id']}.json", 'w') as file:
        json.dump(user_id_list_dicts, file)
