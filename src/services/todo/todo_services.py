from datetime import datetime
import csv
import os

from src.models import Todo
from src.repository import TodoRepository


class TodoService:
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    def save_todo_as_csv(self, todo: Todo, directory="storage"):
        os.makedirs(directory, exist_ok=True)
        date_prefix = datetime.now().strftime("%Y_%m_%d")
        filename = f"{date_prefix}_{todo.id}.csv"
        filepath = os.path.join(directory, filename)

        with open(filepath, 'w', newline='') as csvfile:
            fieldnames = ['userId', 'id', 'title', 'completed']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'userId': todo.user_id, 'id': todo.id, 'title': todo.title, 'completed': todo.completed})

    def save_todos_as_csv(self, directory="storage"):
        todos = self.todo_repository.find_all()
        for todo in todos:
            self.save_todo_as_csv(todo, directory)
