#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

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


def get_completed_todo_titles(todo_list):
    """Returns a list of the titles of the completed TODOs in the list."""

    completed_todo_titles = []
    for todo in todo_list:
        if todo.get('completed') is True:
            completed_todo_titles.append(todo.get('title'))

    return completed_todo_titles


def print_todo_list_progress(
        employee_name,
        completed_todo_titles,
        total_todo_count):
    """Prints the TODO list progress for the given employee."""

    print("Employee {} is done with tasks({}/{}): ".format(employee_name,
          len(completed_todo_titles), total_todo_count))
    for todo_title in completed_todo_titles:
        print("\t {}".format(todo_title))


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    todo_list, user = get_user_todo_list(employee_id)

    completed_todo_titles = get_completed_todo_titles(todo_list)

    print_todo_list_progress(
        user.get('name'),
        completed_todo_titles,
        len(todo_list))
