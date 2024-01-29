#!/usr/bin/python3
""" Script that uses REST API for a given employee ID
and export data in the CSV format.
"""
import requests
from sys import argv


def save_employee_csv():
    base_url = 'https://jsonplaceholder.typicode.com/'
    emp_id = argv[1]

    user_res = requests.get(base_url + 'users/{}'.format(emp_id)).json()
    emp_username = user_res.get('username')

    todos_res = requests.get(base_url + 'todos').json()

    filename = emp_id + ".csv"

    with open(filename, 'w') as f:
        for t in todos_res:
            if t['userId'] == int(emp_id):
                f.write('"{}","{}","{}","{}"\n'
                        .format(emp_id, emp_username,
                                t['completed'], t['title']))


if __name__ == "__main__":
    save_employee_csv()
