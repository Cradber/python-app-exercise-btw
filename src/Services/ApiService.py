import csv
import os
from datetime import datetime
from sys import stderr

import requests


class ApiService:
    def __init__(self):
        self.api = "https://jsonplaceholder.typicode.com/todos/"

    def get_all_todos(self):
        response = requests.get(self.api)
        if response.ok:
            return response.json()
        else:
            response.raise_for_status()

    def save_todo_as_csv(self, todo, dir="storage"):
        date_prefix = datetime.now().strftime("%d_%m_%Y")
        filename = f"{date_prefix}_{todo['id']}.csv"
        filepath = os.path.join(dir, filename)

        with open(filepath, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(todo.keys())
            writer.writerow(todo.values())

    def run(self):
        print('Running ApiService', file=stderr)

        todos = self.get_all_todos()
        for todo in todos:
            self.save_todo_as_csv(todo)
