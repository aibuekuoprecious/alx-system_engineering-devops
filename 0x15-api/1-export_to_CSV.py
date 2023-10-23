#!/usr/bin/python3
""" This module gathers data from an API and writes it to a CSV file """

import csv
import json
import requests
import sys


def get_user_todo_list(employee_id):
    """Returns the TODO list for the given employee ID."""

    url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    url2 = '{}/todos'.format(url1)

    todo_list = requests.get(url2).json()
    user = requests.get(url1).json()

    return todo_list, user


def write_todo_list_to_csv(todo_list, user, employee_id):
    """Writes the TODO list for the given employee to a CSV file."""

    path = "{}.csv".format(employee_id)

    with open(path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerow(['employee_id', 'username', 'completed', 'title'])

        for todo in todo_list:
            writer.writerow([employee_id, user.get('username'),
                            todo.get('completed'), todo.get('title')])


if __name__ == '__main__':
    employee_id = int(sys.argv[1])

    todo_list, user = get_user_todo_list(employee_id)

    write_todo_list_to_csv(todo_list, user, employee_id)
