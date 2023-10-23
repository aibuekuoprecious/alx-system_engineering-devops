#!/usr/bin/python3
"""
Script that uses JSONPlaceholder API to get information about employee and write it to JSON file
"""
import json
import requests
import sys


def get_employee_info(url, userid):
    """
    Returns a JSON object with information about the employee with the given ID.
    """

    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(url, userid)
    res = requests.get(todos)
    tasks = res.json()

    l_task = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        l_task.append(dict_task)

    return {str(userid): l_task}


def write_employee_info_to_json(filename, employee_info):
    """
    Writes the employee information to the given JSON file.
    """

    with open(filename, mode='w') as f:
        json.dump(employee_info, f)


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    userid = sys.argv[1]

    employee_info = get_employee_info(url, userid)

    filename = '{}.json'.format(userid)
    write_employee_info_to_json(filename, employee_info)
