#!/usr/bin/python3
"""
this code will get data from api and process it
"""
import json
from sys import argv
import requests

if __name__ == '__main__':
    """
    main function
    """
    argc = len(argv)
    user_id = argv[1]
    tasks_completed = 0
    number_of_tsks = 0

    api_url_users = 'https://jsonplaceholder.typicode.com/users'
    api_url_todos = 'https://jsonplaceholder.typicode.com/todos'

    result_users = requests.get(api_url_users + '/' + user_id)
    result_todos = requests.get(api_url_todos)

    result_users = json.loads(result_users.text)
    result_todos = json.loads(result_todos.text)

    user_todos = []
    for todo in result_todos:
        if todo['userId'] == int(user_id):
            number_of_tsks += 1
            user_todos.append(todo)
            if todo['completed'] is True:
                tasks_completed += 1

    print(f"Employee {result_users['name']} is done with", end='')
    print(f" tasks({tasks_completed}/{number_of_tsks}):")
    for todo in user_todos:
        if todo['completed'] is True:
            print(f"\t {todo['title']}")
