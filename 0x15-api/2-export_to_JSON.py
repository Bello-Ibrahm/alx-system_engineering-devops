#!/usr/bin/python3
""" Script that uses REST API for a given employee ID
and export data in the json format.
"""
import json
import requests
from sys import argv


def save_employee_json():
    base_url = 'https://jsonplaceholder.typicode.com/'
    emp_id = argv[1]

    user_res = requests.get(base_url + 'users/{}'.format(emp_id)).json()
    emp_username = user_res.get('username')

    todos_res = requests.get(base_url + 'todos?userId={}'.format(emp_id))
    todos_res = todos_res.json()

    filename = emp_id + ".json"

    with open(filename, 'w') as j_file:
        json.dump({emp_id: [{
            "task": t["title"],
            "completed": t["completed"],
            "username": emp_username
            } for t in todos_res]}, j_file)


if __name__ == "__main__":
    save_employee_json()
