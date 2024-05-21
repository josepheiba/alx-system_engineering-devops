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
            todo.update({'username': result_users['username']})
            new_order = ['userId', 'username', 'completed', 'title']
            todo = {key: todo[key] for key in new_order}
            user_todos.append(todo)

    with open(f"{user_todos[0]['userId']}.csv", 'w') as file:
        for todo in user_todos:
            file.write(','.join(f'"{v}"' for v in todo.values()) + '\n')
