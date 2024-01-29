#!/usr/bin/python3
""" Script that uses REST API for a given employee ID
and export data in the json format.
"""
import requests
import json


def save_employee_json():
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_res = requests.get(base_url + 'users').json()

    filename = "todo_all_employees.json"

    with open(filename, 'w') as j_file:
        json.dump({
            u["id"]: [{
            "username": u["username"],
            "task": t["title"],
            "completed": t["completed"],
            } for t in requests.get(base_url + "todos?userId={}".format(u["id"])).json()]
            for u in user_res}, j_file)


if __name__ == "__main__":
    save_employee_json()
