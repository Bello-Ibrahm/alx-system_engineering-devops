#!/usr/bin/python3
""" Script that uses REST API to fetch all  employees
and export data in the json format.
"""
import json
import requests


def save_all_to_dict_json():
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_res = requests.get(base_url + 'users').json()

    filename = "todo_all_employees.json"

    with open(filename, 'w') as j_file:
        json.dump({
            u["id"]: [{
                "username": u["username"],
                "task": t["title"],
                "completed": t["completed"],
            } for t in requests.get(base_url + "todos?userId={}"
                                    .format(u["id"])).json()]
            for u in user_res}, j_file)


if __name__ == "__main__":
    save_all_to_dict_json()
