#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about all employees and write it to JSON file """
import json
import requests
import sys


def get_employee_info(url):
    """
    Returns a JSON object with information about all employees.
    """

    user = '{}users'.format(url)
    res = requests.get(user)
    json_o = res.json()

    d_task = {}
    for user in json_o:
        name = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(url, userid)
        res = requests.get(todos)
        tasks = res.json()

        l_task = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            l_task.append(dict_task)

        d_task[str(userid)] = l_task

    return d_task


def write_employee_info_to_json(filename, employee_info):
    """
    Writes the employee information to the given JSON file.
    """

    with open(filename, mode='w') as f:
        json.dump(employee_info, f)


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    employee_info = get_employee_info(url)

    filename = 'todo_all_employees.json'
    write_employee_info_to_json(filename, employee_info)
