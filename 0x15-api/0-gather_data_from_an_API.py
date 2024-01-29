#!/usr/bin/python3
""" """
import requests
from sys import argv


def getEmployee():
    url = 'https://jsonplaceholder.typicode.com/'

    user_res = requests.get(url + 'users/{}'.format(argv[1])).json()
    user_name = user_res.get('name')

    todos_res = requests.get(url + 'todos').json()

    titles = []
    completed = 0
    total = 0

    for t in todos_res:
        if (t['userId'] == int(argv[1])):
            if (t['completed'] is True):
                completed += 1
                titles.append(t['title'])
            total += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, completed, total))

    for title in titles:
        print("\t {}".format(title))


if __name__ == "__main__":
    getEmployee()
