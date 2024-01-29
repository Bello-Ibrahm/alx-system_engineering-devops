#!/usr/bin/python3
""" Script that uses REST API for a given employee ID
and returns information about the employee TODO list progress."""
import requests
from sys import argv


def get_employee():
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]

    user_res = requests.get(base_url + 'users/{}'.format(user_id)).json()
    user_name = user_res.get('name')

    todos_res = requests.get(base_url + 'todos').json()

    titles = []
    completed = 0
    total = 0

    for t in todos_res:
        if (t['userId'] == int(user_id)):
            if (t['completed'] is True):
                completed += 1
                titles.append(t['title'])
            total += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, completed, total))

    for title in titles:
        print("\t {}".format(title))


if __name__ == "__main__":
    get_employee()
